import { useHistory } from "react-router-dom";

export default function TestLogin() {
    const history = useHistory();

    const onSuccess = (res) => {
        const username = 'charles57';
        history.push(`/discover/${username}`);
    };


    return (
        <div>
            <button onClick={onSuccess}>Test Account Login</button>
        </div>
    )
}
