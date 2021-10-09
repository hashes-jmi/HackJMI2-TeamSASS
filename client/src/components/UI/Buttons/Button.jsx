import React from "react";
import classes from "./Button.module.css";
import Colors from "../../Colors";

function Button(props) {
  return (
    <button
      className={classes["button-theme"]}
      onClick={props.onClick}
      style={{ backgroundColor: Colors.primary }}
    >
      {props.title}
    </button>
  );
}

export default Button;
