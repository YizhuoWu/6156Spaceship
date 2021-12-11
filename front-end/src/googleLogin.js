import { GoogleLogout, GoogleLogin } from "react-google-login";
import { useHistory } from "react-router-dom";
import * as Constants from './constants';

const clientId = Constants.CLIENT_ID;


export default function Login() {
    const history = useHistory();

    const onSuccess = (res) => {
        console.log('[Login Success] currentUser: ', res.profileObj);
        console.log('name: ', res.profileObj.name);
        console.log('email: ', res.profileObj.email);
        const email = res.profileObj.email;
        const username = email.substr(0, email.indexOf('@'))
        console.log('username: ', username);
        history.push(`/search/${username}`);
        // history.push('/auth/google_oauth2/callback');

        // localStorage.getItem('username') === 'undefined';
        localStorage.setItem("username", username);
        alert("local set usnerame = ", username);
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
