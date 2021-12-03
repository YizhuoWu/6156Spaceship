import React, { Component } from 'react';
import MenuBar from './navigation';
import * as Constants from './constants';
import './styles/userProfile.css';

// {"address":"331 Dunn Drives Apt. 490\nWest Melissaview, RI 62632",
// "city":"Amyborough",
// "email":"Veronica.Haynes@columbia.edu",
// "state":"Arkansas",
// "username":"charles57"}


class UserProfile extends Component {

    state = {
        editView: false,
        username: "",
        address: "",
        city: "",
        state: ""
    }

    componentDidMount = () => {
        // charles57
        const { username } = this.props.match.params;
        const userProfileUrl = `${Constants.USER_PROFILE_URL_PREFIX}/${username}`;
        console.log("userProfileUrl: ", userProfileUrl);
        fetch(userProfileUrl) // to be fixed, cors error
            .then(res => res.json())
            .then((data) => {
                console.log("userProfile data: ", data);
            })
            .catch((err) => console.log(err));
    }

    changeEditView = () => {
        // this.setState({
        //     editView: true,
        // });
        this.setState(prevState => ({
            editView: !prevState.editView
        }));
        console.log("change editview: ", this.state.editView);
    }

    saveEditView = () => {
        this.setState((prevState) => ({
            editView: !prevState.editView
        }));
    }

    handleChange = (e) => {
        this.setState({
            [e.target.name]:e.target.value
        })
    }

    render() {
        const { username } = this.props.match.params;
        const email = `${username}@gmail.com`;
        const { pathname } = this.props.location;
        const { editView } = this.state;

        return(
            <div>
                <MenuBar username={username} pathname={pathname} />

                {
                    editView ? 

                    <div class="user-profile">
                        <h2>User Profile</h2>
                        <h3>Email: {email}</h3>
                        <h3>Username: {this.state.username}</h3>
                        <h3>Address: {this.state.address}</h3>
                        <h3>City: {this.state.city}</h3>
                        <h3>State: {this.state.state} </h3>

                        <button onClick={this.changeEditView}>Edit</button>
                        {/* <button onClick={this.saveEditView}>Save</button> */}
                    </div>

                    :

                    <div class="user-profile">
                        <h2>User Profile</h2>
                        <h3>Email: {email}</h3>
                        <h3>Username: </h3><input type="text" name="username" value={this.state.username} onChange={this.handleChange}></input>
                        <h3>Address: </h3><input type="text" name="address" value={this.state.address} onChange={this.handleChange}></input>
                        <h3>City: </h3><input type="text" name="city" value={this.state.city} onChange={this.handleChange}></input> 
                        <h3>State: </h3><input type="text" name="state" value={this.state.state} onChange={this.handleChange}></input>
                        <br /> <br />
                        <button onClick={this.saveEditView}>Save</button>
                        
                    </div>
                }

            </div>
        )
    }
}

export default UserProfile ;