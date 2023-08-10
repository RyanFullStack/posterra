import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import HomePage from "./components/HomePage";
import Community from "./components/Community";
import CommunityForm from "./components/CommunityForm";
import EditCommunity from "./components/EditCommunity";
import PostForm from "./components/PostForm";
import './index.css'

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));

  }, [dispatch]);

  return (
    <div>
      <Navigation isLoaded={isLoaded} />
      <Switch>
        <Route exact path="/" >
          <HomePage />
        </Route>
        <Route path='/communities/new'>
          <CommunityForm />
        </Route>
        <Route path='/posts/new'>
          <PostForm />
        </Route>
        <Route path='/communities/:communityId/edit'>
          <EditCommunity />
        </Route>
        <Route path='/communities/:communityId'>
          <Community />
        </Route>
      </Switch>

    </div>
  );
}

export default App;
