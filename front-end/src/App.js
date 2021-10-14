import logo from './logo.svg';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Discover from './discover';
import UserProfile from './userProfile';
import NewsList from './newsList';
import LoginSignup from './loginSignup';
import './App.css';

function App() {
  return (
    <div className="App">
      <BrowserRouter>

        <Switch>
            <Route exact path='/' component={LoginSignup}/>
            {/* <Route path='/:username/news' component={(props) => <NewsList {...props} />} /> */}
            <Route path='/discover/:username/' component={(props) => <Discover {...props} />} />
            <Route path='/profile/:username/' component={(props) => <UserProfile {...props} />} /> 
            {/* <Route path='/schedule' component={Schedule}/> */}
        </Switch>

      </BrowserRouter>
    </div>
  );
}

export default App;
