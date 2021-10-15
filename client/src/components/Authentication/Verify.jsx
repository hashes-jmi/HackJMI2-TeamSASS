import React, { useState } from "react";
import { useHistory } from "react-router";
import Button from "../UI/Buttons/Button";
import Card from "../UI/Card/Card";
import Input from "../UI/Input/Input";
import classes from "./Verify.module.css";

const Verify = (props) => {
  const history = useHistory();
  const [otp, setOTP] = useState(0);

  const verifyHandler = () => {
    props.toggleLoggedIn();
    history.push("/home");
  };

  return (
    <Card className={classes.verify}>
      <Input
        placeholder="Enter OTP"
        value={otp}
        onChange={(val) => setOTP(val.target.value)}
      />
      <Button onClick={verifyHandler}>Submit OTP</Button>
    </Card>
  );
};

export default Verify;
