import React, { useState } from "react";
import "./App.css";
import { Route, Redirect } from "react-router-dom";
import Home from "./components/Home/Home";
import Map from "./components/Map Stats/Map";
import Navbar from "./components/Navbar/Navbar";
import Login from "./components/Authentication/Login";
import Signup from "./components/Authentication/Signup";
import UserMedicalData from './components/userMedicalData/UserMedicalData'
import Verify from "./components/Authentication/Verify";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const loginHandler = () => {
    setIsLoggedIn(true);
  };
  return (
    <div>
      <Navbar isLoggedIn={isLoggedIn} />
      <Route path="/" exact>
        <Redirect to="/home" />
      </Route>

      <Route path="/login">
        <Login />
      </Route>

      <Route path="/home">
        <Home />
      </Route>

      <Route path="/signup">
        <Signup />
      </Route>
      <Route path="/map">
        <Map />
      </Route>

      <Route path="/verify">
        <Verify toggleLoggedIn={loginHandler} />
      </Route>

    </div>
  );
}

export default App;
