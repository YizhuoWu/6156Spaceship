
import { GoogleLogout, GoogleLogin } from "react-google-login";
import { useHistory } from "react-router-dom";
import * as Constants from './constants';

const clientId = Constants.CLIENT_ID;


export default function Logout() {
    const history = useHistory();
    const onSuccess = (res) => {
        alert('Logout successfully');
        history.push(`/`);
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