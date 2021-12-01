
import { GoogleLogout, GoogleLogin } from "react-google-login";
import { useHistory } from "react-router-dom";


const clientId = "292318877165-fg1mtq4fvdp5mfjujnlikevd7o50p07g.apps.googleusercontent.com"


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