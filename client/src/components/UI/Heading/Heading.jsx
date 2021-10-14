import React from "react";
import classes from "./Heading.module.css";

function Heading(props) {
  return (
    <div className={classes.heading + " " + props.className}>
      <h1>{props.text}</h1>
    </div>
  );
}

export default Heading;
