import React, { Fragment } from "react";
import Button from "../UI/Buttons/Button";
import SecondaryButton from "../UI/Buttons/SecondaryButton";
import classes from "./Navbar.module.css";
import { NavLink } from "react-router-dom";
import Colors from "../Colors";

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
          <a href="/my-e-medcard">My Health ID</a>
        </li>
        {!props.isLoggedIn ? (
          <Fragment>
            <NavLink to="/login">
              <SecondaryButton
                title="Signin"
                onClick={() => console.log("singin")}
              />
            </NavLink>
            <NavLink to="/signup">
              <Button onClick={() => console.log("signup")}>Signup</Button>
            </NavLink>
          </Fragment>
        ) : (
          <Button>
            <ion-icon
              className={classes["ion-icon"]}
              name="person-circle-outline"
              size="large"
            ></ion-icon>
          </Button>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;
