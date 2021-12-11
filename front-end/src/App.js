import logo from './logo.svg';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Discover from './discover';
import UserProfile from './userProfile';
import LoginSignup from './loginSignup';
import Logout from './googleLogout';
import './App.css';
import UserLabelGraph from './details';
import SearchNews from './searchNews';

function App() {

  return (
    <div className="App">
      <BrowserRouter>

        <Switch>
            <Route exact path='/' component={LoginSignup}/>
            <Route path='/login' component={LoginSignup} />

            {/* <Route path='/:username/news' component={(props) => <NewsList {...props} />} /> */}
            <Route path='/discover/:username/' component={(props) => <Discover {...props} />} />
            <Route path='/profile/:username/' component={(props) => <UserProfile {...props} />} /> 
            <Route path='/detail/:username/' component={(props) => <UserLabelGraph {...props} />} />
            <Route path='/search/:username/' component={(props) => <SearchNews {...props} />} />

            {/* <Route path='/auth/google_oauth2/callback' component={(props) => <Discover {...props} />} /> */}

            <Route path='/logout' component={(props) => <Logout {...props} />} />
            {/* <Route path='/schedule' component={Schedule}/> */}
        </Switch>

      </BrowserRouter>
    </div>
  );
}

export default App;
