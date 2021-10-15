import React from "react";
import classes from "./Login.module.css";
import Card from "../UI/Card/Card";
import Button from "../UI/Buttons/Button";
import { useState } from "react";
import axios from "axios";
function Login() {
  const [addhar,setaadhar]=useState('');

  return (
    <Card className={classes["login-modal"]}>
      <div className={classes.heading}>Login</div>
      <input type="number" placeholder="Enter Adhar Number..." onChange={(e)=>{setaadhar(e.target.value)}} value={addhar} />
      <Button title="Send OTP" onClick={(e)=>{
        axios.post()
      }} />
      <p>Don’t have an account? Sign up here!</p>
    </Card>
  );
}

export default Login;
