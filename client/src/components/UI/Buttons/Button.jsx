import React from "react";
import Colors from "../../Colors";
import classes from "./Button.module.css";

function Button(props) {
  return (
    <button className={classes["button-theme"]} onClick={props.onClick}>
      {props.title}
    </button>
  );
}

export default Button;
