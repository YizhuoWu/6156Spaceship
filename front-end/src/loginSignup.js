import React, { Component, useState } from 'react';
import { useHistory } from "react-router-dom";
import { GoogleLogout, GoogleLogin } from "react-google-login";
import { refreshTokenSetup } from './utils/refreshToken';
import Login from './googleLogin';
import Logout from './googleLogout';
// import MenuBar from './navigation';

const prefixUrl = "https://em85ugzj5d.execute-api.us-east-1.amazonaws.com/v1"
const loginPageUrl = `${prefixUrl}/profile`;


const responseGoogle = (response) => {
    console.log(response);
}

class LoginSignup extends Component {

    state = {
        username: "",
        password: "",
        signUpView: false,
    }

    componentDidMount = () => {
        fetch(loginPageUrl)
            .then(res => res.json())
            .then((res) => {
                console.log("res: ", res)
            })
    }

    switchView = () => {
        this.setState((prevState) => ({
            signUpView: !prevState.signUpView
        }));
    }

    render() {
        const buttonName = this.state.signUpView ? "Login" : "SignUp"

        return(
            <div className="login">

                <h1>NewsFeed</h1>
        

                {/* <button onClick={this.submitAuthInfo} >
                    Redirect
                </button> */}

                {/* <button onClick={this.switchView}>
                    {buttonName}
                </button> */}

                <br /> <br />
 
                <Login />
                {/* <Logout />
                 */}
            
            </div>
        )
    }
}

export default LoginSignup;