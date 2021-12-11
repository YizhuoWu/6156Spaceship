import React, { Component } from 'react';
import MenuBar from './navigation';
import * as Constants from './constants';
import './styles/discover.css';


// ref: https://newsapi.org/docs/get-started
const API_KEY =  Constants.API_KEY;
const urlPrefix = "https://newsapi.org/v2/everything"


// props: username, newsId, title, description, imageUrl
class NewsItem extends Component {
    state = {
        commentView: false,
        userInput: "",
        comments: [],
        numLikes: 0
    }

    componentDidMount = () => {
        const { newsId } = this.props;

        // get num likes
        const newsLikesUrl = `${Constants.LIKES_URL_PREFIX}?newsid=${newsId}`;
        // console.log("newsLikesUrl: ", newsLikesUrl);

        fetch(newsLikesUrl)
            .then(res => res.json())
            .then((data) => {
                // console.log("fetch news likes data for newsid=", newsId);
                // console.log("likes data: ", data.num_likes);
                this.setState({
                    numLikes: data.num_likes
                })
            })
            .catch(error => console.log('NEwsItem ComponentDidmout Fetch Likes Error! ' + error.message));

    }

    userInputOnChange = (e) => {
        this.setState({
            [e.target.name]:e.target.value
        })
    }

    // click (display)comment button
    commentHandler = (newsId) => {

        // display comment view
        this.setState((prevState) => ({
            commentView: !prevState.commentView
        }))
        // clear comments
        // this.setState({
        //     comments: []
        // }) 

        const newsCommentUrl = `${Constants.COMMENT_URL_PREFIX}/${newsId}`; // <newsid>
        console.log("newsCommentUrl: ", newsCommentUrl);

        fetch(newsCommentUrl)
            .then(res => res.json())
            .then((data) => {
                console.log("news comments length:", data.comments.length);
                
                // news_id, content_full, comments
                if (typeof data === 'undefined' || typeof data.news === 'undefined' || typeof data.news.comments === 'undefined') {
                    return;
                }
                data.comments.forEach((comment, index) => {
                    console.log("comment.usernmae: ", comment.username);
                    this.setState((prevState) => ({
                        comments: [...prevState.comments, {
                            username: comment.username,
                            timestamp: comment.timestamp,
                            comment_info: comment.comment_info
                        }]
                    }));
                });
            })
    }//commentHandler

    postComment = () => {
        const { newsId, username } = this.props;
        const newsCommentUrl = `${Constants.COMMENT_URL_PREFIX}/post`;
        
        console.log("newsCommentUrl", newsCommentUrl);
        console.log("newsId: ", newsId, ", username: ", username);
        console.log("postComment, userInput: ", this.state.userInput);
        const currentTime = new Date().toLocaleString();
        const commentInfo = this.state.userInput;

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(
                {
                    "news_id": parseInt(newsId),
                    "username": username,
                    "comment_info": commentInfo
                }
            )
        };
        fetch(newsCommentUrl, requestOptions)
            .then(response => response.json())
            .then((data) => {
                this.setState((prevState) => ({
                    comments: [...prevState.comments, {
                        username: username,
                        timestamp: currentTime,
                        comment_info: commentInfo
                    }]
                }));
            });

        // reset userInput
        this.setState({
            userInput: ""
        })
    }

    postLike = (newsId) => {
        // get num likes
        const newsLikesUrl = `${Constants.LIKES_URL_PREFIX}`;
        const { username } = this.props;

        const requestOptions = {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                newsid: newsId,
                username: username
            })
        };

        console.log("newsLikesUrl: ", newsLikesUrl);
        fetch(newsLikesUrl, requestOptions)
            .then(res => res.json())
            .then((data) => {
                // console.log("fetch news likes data for newsid=", newsId);
                console.log("post likes data: ", data.body);
                data = JSON.parse(data.body)
                // console.log("likes data access: ", data["num_likes"]);  
                this.setState({
                    numLikes: data["num_likes"]
                })
            })
            .catch(error => console.log('Fetch Likes Error! ' + error.message));


    }

    render() {
        const { newsId, title, description, imageUrl } = this.props;
        const { commentView, numLikes } = this.state;
        const placeHolderText = `comment for news ${newsId}`;
        
        const renderedLikes = <div class="likes">
            <button id="like_button" onClick={() => this.postLike(newsId)}></button>
            &nbsp;
            <b>{numLikes}</b>
        </div>
        
        const renderedComments = this.state.comments.map((comment, i) => 
            <div key={i} class="comment-list">
                <b>{comment.username}</b> 
                &nbsp; &nbsp; &nbsp;
                <div class="inline-block:left">
                    <p>{comment.timestamp}</p>
                </div>
                <p>{comment.comment_info}</p>
            </div>
        );

        return (
            <div class="news-item">
                <h2>{title}</h2>
                <p>{description}</p>

                <img src={imageUrl} alt="image url" />

                {renderedLikes}

                <div onClick={() => this.commentHandler(newsId)}>
                    <button id="comment_button">.</button>
                    <b>Comment</b>
                </div>
                
                {commentView ?
                    <div class="comment">
                        <div class="comment-content">
                            {renderedComments}
                        </div>
                        <input type="text" placeholder={placeHolderText} name="userInput" value={this.state.userInput} onChange={this.userInputOnChange}></input>  
                        <button id="post_button" onClick={this.postComment}>Post</button>  
                    </div>
                    :
                    <div></div>
                }
            </div>
        )
    }
}

// props: newsList, username
class NewsList extends Component {
    render() {
        const renderedNewsList = this.props.newsList.map((newsItem, i) => (
            <div key={i}>
                <NewsItem 
                    username={this.props.username}
                    newsId={newsItem.newsId}
                    title={newsItem.title}
                    description={newsItem.description}
                    imageUrl={newsItem.imageUrl}
                />
            </div>
        ));

        return(
            <div>
                {renderedNewsList}
            </div>
        )
    }
}


class SearchNews extends Component {

    state = {
        userInput: '',
        newsList: []
    }

    changeUserInput = (e) => {
        this.setState({
            userInput: e.target.value,
        })
    }


    searchNews = () => {
        // const searchNewsUrl = `${urlPrefix}?q=${this.state.userInput}&apiKey=${API_KEY}`;
        const { userInput } = this.state;
        const searchNewsUrl = `${Constants.NEWS_SERVICE_PREFIX}/search?query=${userInput}`;
        console.log("searchNewsUrl: ", searchNewsUrl);

        fetch(searchNewsUrl)
            .then(res => res.json())
            .then((data) => {
                console.log("searchNews data: ", data);
                if (typeof data.articles === 'undefined') {
                    return;
                }
                const articles = data.articles.slice(0, 10);
                articles.forEach((article, index) => {
                    this.setState((prevState) => ({
                        newsList: [...prevState.newsList, {
                            newsId: article.id, // index.toString(),
                            title: article.title,
                            description: article.description,
                            imageUrl: article.image_url
                        }]
                    }));
                });//articles
            })//then

        this.setState({
            userInput: ''
        })
    }//searchNews


    render() {
        const { username } = this.props.match.params;
        const { pathname } = this.props.location;
        const { newsList } = this.state;

        return(
            <div>
                <MenuBar username={username} pathname={pathname}/>
                

                <div class="search-bar">  
 
                    <input type="text" value={this.state.userInput} 
                        onChange={this.changeUserInput}
                        placeholder="What news are you looking for?">
                    </input>  
                    
                    <button onClick={this.searchNews}>
                        Search
                    </button>       

                    {/* <div class="user-labels">
                        {renderedUserLabels}
                    </div>      */}
                </div>

                <NewsList newsList={newsList} username={username} />

            </div>
        )
    }
}

export default SearchNews;
