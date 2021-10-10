import React, { Component, useState } from 'react';
import { useHistory } from "react-router-dom";

const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    // const { authenticate } = useContext(AccountContext);

    const history = useHistory();


    const onSubmit = (e) => {
        e.preventDefault();
        console.log("username: ", username)
        history.push(`/discover/${username}/`);
    };

    return(
        <div>
            <form onSubmit={onSubmit}>
                <label htmlFor="username">username</label>
                <input placeholder="username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                ></input>
                <br/>
                <br/>
                <label htmlFor="password">password</label>
                <input placeholder="password"
                    value={password}
                    onChange={(e)=> setPassword(e.target.value)}
                ></input>
                <br/>
                <br />
                <button type="submit">Login</button>
            </form>
        </div>
    );
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