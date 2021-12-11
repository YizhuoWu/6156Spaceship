import React, { Component, useState } from 'react';
import { useHistory } from "react-router-dom";
import Login from './googleLogin';
import TestLogin from './testLogin';
// import MenuBar from './navigation';
import './styles/loginSignup.css';

const prefixUrl = "https://em85ugzj5d.execute-api.us-east-1.amazonaws.com/v1"
const loginPageUrl = `${prefixUrl}/profile`;


export default function LoginSignup() {
    const history = useHistory();

    // if (localStorage.getItem('username') === 'undefined') {
    //     console.log("username===undefine");
    // } else {
    //     const username = localStorage.getItem('username');
    //     history.push(`/discover/${username}`);
    // }

    return(
        <div class="login">

            <body>
                <h1>NewsFeed</h1>

                <br /> <br />
                <Login/>

                <br /> <br />
                <TestLogin />
            </body>
        
        </div>
    )
}
