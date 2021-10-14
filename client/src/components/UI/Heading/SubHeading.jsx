import React from "react";
import classes from "./SubHeading.module.css";

function Heading(props) {
  return (
    <div className={classes.heading + " " + props.className}>
      <h2>{props.text}</h2>
    </div>
  );
}

export default Heading;
