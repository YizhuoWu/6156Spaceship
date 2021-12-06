import React, { Component } from 'react';
import { Navigation } from 'react-minimal-side-navigation';
import { useHistory } from "react-router-dom";
import 'react-minimal-side-navigation/lib/ReactMinimalSideNavigation.css';
import './styles/menuBar.css';


// props: 
// ref: https://reactjsexample.com/minimal-side-navigation-component-for-react/
const MenuBar = (props) => {
    const history = useHistory();
    const { username, pathname } = props;
    return (
        <div class="menu-bar">
            <Navigation
                // you can use your own router's api to get pathname
                activeItemId={pathname}
                onSelect={({itemId}) => {
                    // maybe push to the route
                    console.log("itemId: ", itemId);
                    history.push(itemId);
                }}
                items={[
                {
                    title: 'Discover',
                    itemId: `/discover/${username}`,
                    // you can use your own custom Icon component as well
                    // icon is optional
                    //elemBefore: () => <Icon name="inbox" />,
                },
                {
                    title: 'Profile',
                    itemId: `/profile/${username}`,
                    //elemBefore: () => <Icon name="users" />,
                //   subNav: [
                //     {
                //       title: 'Projects',
                //       itemId: '/management/projects',
                //     },
                //     {
                //       title: 'Members',
                //       itemId: '/management/members',
                //     },
                //   ],
                },
                {
                    title: 'Logout',
                    itemId: '/logout',
                //   subNav: [
                //     {
                //       title: 'Teams',
                //       itemId: '/management/teams',
                //     },
                //   ],
                },
                ]}//items
            />
        </div>
    );
}

export default MenuBar;
