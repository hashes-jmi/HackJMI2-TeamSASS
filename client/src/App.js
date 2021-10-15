import "./App.css";
import { Route, Redirect } from "react-router-dom";
import Home from "./components/Home/Home";
import Map from "./components/Map Stats/Map";
import Navbar from "./components/Navbar/Navbar";
import Login from "./components/Authentication/Login";
import Signup from "./components/Authentication/Signup";
import UserMedicalData from './components/userMedicalData/UserMedicalData'
function App() {
  return (
    <div>
      <Navbar />
      <Route path="/" exact>
        <Redirect to="/home" />
      </Route>

      <Route path="/">
        <Home />home
      </Route>

      <Route path="/login">
        <Login />
      </Route>

      <Route path="/signup">
        <Signup />
      </Route>
      <Route path="/map">
        <Map />
      </Route>
      
    </div>
  );
}

export default App;
