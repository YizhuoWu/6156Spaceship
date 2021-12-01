import React, { Component } from 'react';
import MenuBar from './navigation';


class UserProfile extends Component {

    render() {
        const { username } = this.props.match.params;
        const { pathname } = this.props.location;

        return(
            <div>
                This is UserProfile
                <MenuBar username={username} pathname={pathname} />

            </div>
        )
    }
}

export default UserProfile ;