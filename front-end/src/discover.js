import React, { Component } from 'react';


class Discover extends Component {

    state = {
        userInput: ""
    }

    changeUserInput = (e) => {
        this.setState({
            userInput: e.target.value,
        })
    }

    searchNews = () => {
        console.log("serach news!")
    }

    render() {
        return(
            <div>
                This is Discover Page
                <div className="searchBar">  
                    <span>                   
                        {/* <label>Search News: </label>             */}
                        <input type="text" value={this.state.userInput} 
                            onChange={this.changeUserInput}
                            placeholder="What news are you looking for?">
                        </input>  
                        <input type="submit" value="Search"
                            onClick={this.searchNews}
                        ></input>  
                    </span>                  
                </div>

            </div>
        )
    }
}

export default Discover;