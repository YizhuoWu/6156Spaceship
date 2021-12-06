import React, { Component, useState } from 'react';
import Login from './googleLogin';
import TestLogin from './testLogin';
// import MenuBar from './navigation';

const prefixUrl = "https://em85ugzj5d.execute-api.us-east-1.amazonaws.com/v1"
const loginPageUrl = `${prefixUrl}/profile`;


class LoginSignup extends Component {

    state = {
        username: "",
        password: "",
        signUpView: false,
    }

    componentDidMount = () => {
        // fetch(loginPageUrl)
        //     .then(res => res.json())
        //     .then((res) => {
        //         console.log("res: ", res)
        //     })
    }

    switchView = () => {
        this.setState((prevState) => ({
            signUpView: !prevState.signUpView
        }));
    }


    render() {

        return(
            <div className="login">

                <h1>NewsFeed</h1>

                <br /> <br />
                <Login/>

                 <br /> <br />
                 <TestLogin />
            
            </div>
        )
    }
}

export default LoginSignup;