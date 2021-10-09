import React from "react";
import Button from "../UI/Buttons/Button";
import SecondaryButton from "./../UI/Buttons/SecondaryButton";
import classes from "./Navbar.module.css";

const Navbar = (props) => {
  const flexRowAlignClass = classes["flex-row-align"];
  const navbarClass = classes.navbar + " " + flexRowAlignClass;
  const authLinksClasses = classes.authentication + " " + flexRowAlignClass;
  return (
    <nav className={navbarClass}>
      <ul className={flexRowAlignClass}>
        <li>
          <a href="/home">Home</a>
        </li>
        <li>
          <a href="/map">MapStats</a>
        </li>
      </ul>
      <ul className={authLinksClasses}>
        <li>
          <a href="/my-e-medcard">My e-MedCard</a>
        </li>
        <SecondaryButton title="Signin" onClick={() => console.log("singin")} />
        <Button title="Signup" onClick={() => console.log("signup")} />
      </ul>
    </nav>
  );
};

export default Navbar;
