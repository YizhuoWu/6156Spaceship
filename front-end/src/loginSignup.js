import React, { Component } from 'react';


class Login extends Component {

    state = {
        username: "",
        password: ""
    }

    onSubmit = (e) => {
        e.preventDefault();
    }

    setUsername = (text) => {
        this.setState({
            username: text
        })
    }

    setPassword = (text) => {
        this.setState({
            password: text
        })
    }

    render() {
        let {username, password} = this.state;
        return(
            <div>
                <form onSubmit={this.onSubmit}>
                    <label htmlFor="username">username</label>
                    <input placeholder="username"
                        value={username}
                        onChange={(e) => this.setUsername(e.target.value)}
                    ></input>
                    <br/>
                    <br/>
                    <label htmlFor="password">password</label>
                    <input placeholder="password"
                        value={password}
                        onChange={(e)=> this.setPassword(e.target.value)}
                    ></input>
                    <br/>
                    <br />
                    <button type="submit">Login</button>
                </form>
            </div>
        );
    }
}

class LoginSignup extends Component {

    state = {
        username: "",
        password: "",
        signUpView: false,
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

                <h1></h1>

                {/* <button onClick={this.submitAuthInfo} >
                    Redirect
                </button> */}

                <button onClick={this.switchView}>
                    {buttonName}
                </button>
                <br /> <br />
 
                {this.state.signUpView ? 
                    <Login />
                :
                    <Login />
                }
            
            </div>
        )
    }
}

export default LoginSignup;