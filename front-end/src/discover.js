import React, { Component } from 'react';
import { useHistory } from "react-router-dom";
import MenuBar from './navigation';
import * as Constants from './constants';
import './styles/newsList.css';

// ref: https://newsapi.org/docs/get-started
const API_KEY =  Constants.API_KEY;
const urlPrefix = "https://newsapi.org/v2/everything"


// props: username, newsId, title, description
class NewsItem extends Component {
    state = {
        commentView: false,
        userInput: "",
        comments: []
    }

    componentDidMount = () => {
        const { newsId } = this.props;
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
        this.setState({
            comments: []
        }) 

        const newsCommentUrl = `${Constants.COMMENT_URL_PREFIX}/${newsId}`; // <newsid>
        console.log("newsCommentUrl: ", newsCommentUrl);

        fetch(newsCommentUrl)
            .then(res => res.json())
            .then((data) => {
                // news_id, content_full, comments
                if (typeof data === 'undefined' || typeof data.news === 'undefined' || typeof data.news.comments === 'undefined') {
                    return;
                }
                data.news.comments.forEach((comment, index) => {
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
                    "news_id": newsId,
                    "username": username,
                    "comment_info": commentInfo,
                    "timestamp": currentTime
                }
            )
        };
        fetch(newsCommentUrl, requestOptions)
            .then(response => response.json())
            .then((data) => {
                console.log("post comment: ", data);
                this.setState((prevState) => ({
                    comments: [...prevState.comments, {
                        username: username,
                        timestamp: currentTime,
                        comment_info: commentInfo
                    }]
                }));
            });
    }

    render() {
        const { newsId, title, description } = this.props;
        const { commentView } = this.state;
        const placeHolderText = `comment for news ${newsId}`;
        const renderedComments = this.state.comments.map((comment, i) => 
            <div key={i}>
                <b>{comment.comment_info}</b>
                <p>{comment.username} | {comment.timestamp}</p>
            </div>
        );

        return (
            <div class="news-item">
                <h3>{title}</h3>
                <p>{description}</p>
                <button onClick={() => this.commentHandler(newsId)}>Comment</button>
                
                {commentView ?
                    <div>
                        {renderedComments}
                        <input type="text" placeholder={placeHolderText} name="userInput" value={this.state.userInput} onChange={this.userInputOnChange}></input>  
                        <button onClick={this.postComment}>post</button>  
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


class Discover extends Component {

    state = {
        userInput: "",
        newsList: []
    }

    changeUserInput = (e) => {
        this.setState({
            userInput: e.target.value,
        })
    }

    // news feed api
    searchNews = () => {
        const searchNewsUrl = `${urlPrefix}?q=${this.state.userInput}&apiKey=${API_KEY}`;
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
                            newsId: index,
                            title: article.title,
                            description: article.description
                        }]
                    }));
                });//articles
            })//then
    }//searchNews

    getNewsComment = () => {
        const { username } = this.props.match.params;
        const newsId = 1;
        const newsCommentUrl = `${Constants.COMMENT_URL_PREFIX}/${username}/${newsId}`; // username/newsid
        
    }

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
                </div>

                <NewsList newsList={newsList} username={username} />
            </div>
        )
    }//render
}

export default Discover;