import React from "react";
import Card from "../UI/Card/Card";
import Heading from "../UI/Heading/Heading";
import SubHeading from "../UI/Heading/SubHeading";
import Input from "../UI/Input/Input";
import classes from "./Signup.module.css";

function Signup(props) {
  return (
    <Card className={classes.signup}>
      <Heading className={classes.heading} text="Create Your Account" />
      <div className={classes["signup-inputs-container"]}>
        <div className={classes["custom-input-container"]}>
          <label htmlFor="create-first-name">First Name</label>
          <Input
            type="text"
            onChange={() => console.log("hello")}
            placeholder="Enter First Name..."
            className={classes.input}
            id="create-first-name"
          />
        </div>
        <div className={classes["custom-input-container"]}>
          <label htmlFor="create-last-name">Last Name</label>
          <Input
            type="text"
            onChange={() => console.log("hello")}
            placeholder="Enter Last Name..."
            className={classes.input}
            id="create-last-name"
          />
        </div>

        <div className={classes["custom-input-container"]}>
          <label htmlFor="create-dob">Date of Birth</label>
          <Input type="date" id="create-dob" />
        </div>

        <div
          className={classes.gender + " " + classes["custom-input-container"]}
        >
          <label htmlFor="create-male">Male</label>
          <Input id="create-male" type="radio" />

          <label htmlFor="create-female">Female</label>
          <Input id="create-female" type="radio" />
        </div>

        <div className={classes["custom-input-container"]}>
          <label htmlFor="create-address">Full Address</label>
          <Input
            type="address"
            placeholder="Enter address..."
            id="create-address"
          />
        </div>

        <div className={classes["custom-input-container"]}>
          <label htmlFor="create-phone-number">Phone Number</label>
          <Input
            type="tel"
            placeholder="Enter Phone..."
            id="create-phone-number"
          />
        </div>

        <div className={classes["custom-input-container"]}>
          <label htmlFor="create-email">E-mail</label>
          <Input type="email" placeholder="Enter Email..." id="create-email" />
        </div>

        <div className={classes["custom-input-container"]}>
          <label htmlFor="create-aadhaar">Aadhaar Number</label>
          <Input
            type="tel"
            placeholder="Enter Aadhaar..."
            id="create-aadhaar"
            maxLength={12}
          />
        </div>
      </div>
      <SubHeading text="Medical Details" className={classes.heading} />
      <div className={classes.signup}></div>
    </Card>
  );
}

export default Signup;
