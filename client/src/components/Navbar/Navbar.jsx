import React from "react";
import Button from "../UI/Buttons/Button";

const Navbar = () => {
  return (
    <nav>
      <ul>
        <li>
          <a href="/home">Home</a>
        </li>
        <li>
          <a href="/map">Map Stats</a>
        </li>
      </ul>
      <ul>
        <li>
          <a href="/my-e-medcard">My e-MedCard</a>
        </li>
        <button>Sign in</button>
        <Button title="Signup" onClick={() => console.log("signup")} />
      </ul>
    </nav>
  );
};

export default Navbar;
