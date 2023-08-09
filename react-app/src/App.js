import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import HomePage from "./components/HomePage";
import Community from "./components/Community";

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
        <Route path='/communities/:communityId'>
          <Community />
        </Route>
      </Switch>

    </div>
  );
}

export default App;
