import { GoogleLogout, GoogleLogin } from "react-google-login";
import { useHistory } from "react-router-dom";


const clientId = "292318877165-fg1mtq4fvdp5mfjujnlikevd7o50p07g.apps.googleusercontent.com"


export default function Login() {
    const history = useHistory();

    const onSuccess = (res) => {
        console.log('[Login Success] currentUser: ', res.profileObj);
        console.log('name: ', res.profileObj.name);
        console.log('email: ', res.profileObj.email);
        const email = res.profileObj.email;
        const username = email.substr(0, email.indexOf('@'))
        console.log('username: ', username);
        history.push(`/discover/${username}`);
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
