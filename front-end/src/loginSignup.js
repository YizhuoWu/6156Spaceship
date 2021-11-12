import React, { Component, useState } from 'react';
import { useHistory } from "react-router-dom";
import { GoogleLogout, GoogleLogin } from "react-google-login";
import { refreshTokenSetup } from './utils/refreshToken';

const clientId = "292318877165-fg1mtq4fvdp5mfjujnlikevd7o50p07g.apps.googleusercontent.com"
const prefixUrl = "https://em85ugzj5d.execute-api.us-east-1.amazonaws.com/v1"
const loginPageUrl = `${prefixUrl}/profile`;


const responseGoogle = (response) => {
    console.log(response);
}

// const Login = () => {
//     const [username, setUsername] = useState("");
//     const [password, setPassword] = useState("");

//     // const { authenticate } = useContext(AccountContext);

//     const history = useHistory();

//     // submit to back end api gateway for auth
//     const onSubmit = (e) => {
//         e.preventDefault();
//         console.log("username: ", username)
//         console.log("password: ", password)

//         const requestOptions = {
//             method: 'POST',
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify({ 
//                 username: username,
//                 password: password,
//             })
//         };
//         fetch(loginPageUrl, requestOptions)
//             .then(res => res.json())
//             .then((res) => {
//                 console.log("post request result: ", res)
//             });
//         //history.push(`/discover/${username}/`);
//     };

//     return(
//         <div>
//             <form onSubmit={onSubmit}>
//                 <label htmlFor="username">username</label>
//                 <input placeholder="username"
//                     value={username}
//                     onChange={(e) => setUsername(e.target.value)}
//                 ></input>
//                 <br/>
//                 <br/>
//                 <label htmlFor="password">password</label>
//                 <input placeholder="password"
//                     value={password}
//                     onChange={(e)=> setPassword(e.target.value)}
//                 ></input>
//                 <br/>
//                 <br />
//                 <button type="submit">Login</button>

//             </form>
//         </div>
//     );
// }


function Login() {
    const history = useHistory();

    const onSuccess = (res) => {
        console.log('[Login Success] currentUser: ', res.profileObj);
        history.push(`/`);
    };

    const onFailure = (res) => {
        console.log('[Login failed] res: ', res);
    };

    return (
        <div>
            <GoogleLogin
                clientId={clientId}
                buttonText="login"
                onSuccess={onSuccess}
                onFailure={onFailure}
                cookiePolicy={'single_host_origin'}
                style={{ marginTop:'100px' }}
                isSignedIn={true}
            />
        </div>
    )
}

function Logout() {
    const onSuccess = (res) => {
        alert('Logout successfully');
    }
    return (
        <div>
            <GoogleLogout
                clientId={clientId}
                buttonText='Logout'
                onLogoutSuccess={onSuccess}
            />
        </div>
    )
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
                <Logout />
            
            
            </div>
        )
    }
}

export default LoginSignup;