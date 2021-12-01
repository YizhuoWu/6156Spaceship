import React, { Component } from 'react';
import { useHistory } from "react-router-dom";
import MenuBar from './navigation';
import * as Constants from './constants';
import './styles/newsList.css';

// ref: https://newsapi.org/docs/get-started
const API_KEY =  Constants.API_KEY;
const urlPrefix = "https://newsapi.org/v2/everything"


// props: title, description
class NewsItem extends Component {
    render() {
        const { title, description } = this.props;
        return (
            <div class="news-item">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
        )
    }
}

// props: newsList
class NewsList extends Component {
    render() {
        const renderedNewsList = this.props.newsList.map((newsItem, i) => (
            <div key={i}>
                <NewsItem 
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

    searchNews = () => {
        console.log("serach news!")
        const searchNewsUrl = `${urlPrefix}?q=${this.state.userInput}&apiKey=${API_KEY}`;
        fetch(searchNewsUrl)
            .then(res => res.json())
            .then((data) => {
                console.log("searchNews data: ", data);
                if (typeof data.articles === 'undefined') {
                    return;
                }
                const articles = data.articles.slice(0, 10);
                articles.forEach((article) => {
                    this.setState((prevState) => ({
                        newsList: [...prevState.newsList, {
                            title: article.title,
                            description: article.description
                        }]
                    }));
                });//articles
            })//then
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
                </div>

                <NewsList newsList={newsList}/>
            </div>
        )
    }//render
}

export default Discover;