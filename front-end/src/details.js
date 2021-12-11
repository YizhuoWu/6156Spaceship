import React, { Component } from 'react';
import MenuBar from './navigation';
import ViewFreqChart from './barChart';
import './styles/barChart.css';
import * as Constants from './constants';


class UserLabelGraph extends Component {

    componentDidMount = () => {
        console.log("this is user details page");
        const { username } = this.props.match.params;
        const fetchUserLabelUrl = `${Constants.USER_LABELS_URL_PREFIX}?username=${username}`;
        fetch(fetchUserLabelUrl)
            .then((res) => res.json())
            .then((data) => {
                
                console.log("username: ", data.username);
                console.log("labels: ", data.labels);
                Object.keys(data.labels).forEach((label) => {
                    console.log(label, data.labels[label]);
                });
                
                localStorage.setItem("user-labels", data.labels);
                console.log(localStorage.getItem("user-labels"));
                // Object.keys(localStorage.getItem("user-labels")).forEach((label) => {
                //     console.log(label)
                // })

            })
            .catch((err) => console.log(err));
    }   

    render() {
        const { username } = this.props.match.params;
        const { pathname } = this.props.location;
        console.log(username, pathname);

        return(
            <div>
                <MenuBar username={username} pathname={pathname} />
                This is User Label Graph.
                <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.min.js"></script>
                <ViewFreqChart />
            </div>
        )
    }
}

export default UserLabelGraph;
