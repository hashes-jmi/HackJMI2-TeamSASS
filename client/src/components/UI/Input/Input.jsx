import React, { Fragment } from "react";
import classes from "./Input.module.css";

function Input(props) {
  return (
    <input
      id={props.id}
      type={props.type}
      placeholder={props.placeholder}
      className={classes["custom-input"] + " " + props.className}
      onChange={(val) => props.onChange(val)}
      maxLength={props.maxLength}
      {...props}
    />
  );
}

export default Input;
