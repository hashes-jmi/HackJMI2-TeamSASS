import React from "react";
import Colors from "../../Colors";
import classes from "./SecondaryButton.module.css";

function SecondaryButton(props) {
  return (
    <button className={classes["button-theme"]} onClick={props.onClick}>
      {props.title}
    </button>
  );
}

export default SecondaryButton;
