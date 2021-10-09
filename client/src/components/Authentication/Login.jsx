import React from "react";
import classes from "./Login.module.css";
import Card from "../UI/Card/Card";
import Button from "../UI/Buttons/Button";
function Login() {
  return (
    <Card className={classes["login-modal"]}>
      <div className={classes.heading}>Login</div>
      <input type="number" placeholder="Enter Adhar Number..." />
      <Button title="Send OTP" />
      <p>Don’t have an account? Sign up here!</p>
    </Card>
  );
}

export default Login;
