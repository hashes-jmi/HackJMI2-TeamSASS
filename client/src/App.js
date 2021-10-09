import "./App.css";
import { Route } from "react-router-dom";
import Home from "./components/Home/Home";
import Map from "./components/Map Stats/Map";
import Navbar from "./components/Navbar/Navbar";

function App() {
  return (
    <div className="App">
      <Navbar />
      <Route path="/home">
        <Home />
      </Route>

      <Route path="/map">
        <Map />
      </Route>
    </div>
  );
}

export default App;
