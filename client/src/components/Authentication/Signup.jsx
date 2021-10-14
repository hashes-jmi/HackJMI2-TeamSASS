import React, { useState } from "react";
import Button from "../UI/Buttons/Button";
import Card from "../UI/Card/Card";
import Heading from "../UI/Heading/Heading";
import Input from "../UI/Input/Input";
import classes from "./Signup.module.css";
import axios from "axios";

function Signup(props) {
  const URL = `https://mhodsaifansari.pythonanywhere.com`;
// const URL=`http://127.0.0.1:8000`
  const [userData, setUserData] = useState({
    firstName: "",
    lastName: "",
    phone: "",
    email: "",
    aadhar: "",
    address: {
      country: "India",
      state: "",
      pincode: "",
      line_1: "",
    },
  });

  const submitHandler = async (e) => {
    e.preventDefault();
    console.log(userData);
    const requestObject = {
      "name": userData.firstName + " " + userData.lastName,
      "phone": +userData.phone,
      "email": userData.email,
      "aadhar": +userData.aadhar,
      
      "address": {
        "country": userData.address.country,
        "state": userData.address.state,
        "pincode": userData.address.pincode,
        "line1": userData.address.line_1,
      },
    };
    console.log(requestObject);
     const response = axios.post(`${URL}/register`,requestObject)
    const resData = await response.json();

    // console.log(resData);
  };

  return (
    <Card className={classes.signup}>
      <form onSubmit={submitHandler}>
        <Heading className={classes.heading} text="Create Your Account" />
        <div className={classes["signup-inputs-container"]}>
          <div className={classes["custom-input-container"]}>
            <label htmlFor="create-first-name">First Name</label>
            <Input
              type="text"
              onChange={(val) =>
                setUserData((state) => {
                  return { ...state, firstName: val.target.value };
                })
              }
              placeholder="Enter First Name..."
              id="create-first-name"
            />
          </div>

          <div className={classes["custom-input-container"]}>
            <label htmlFor="create-last-name">Last Name</label>
            <Input
              type="text"
              onChange={(val) =>
                setUserData((state) => {
                  return { ...state, lastName: val.target.value };
                })
              }
              placeholder="Enter Last Name..."
              id="create-last-name"
            />
          </div>

          <div className={classes["custom-input-container"]}>
            <label htmlFor="create-address">Address</label>
            <Input
              type="address"
              placeholder="Enter address..."
              id="create-address"
              onChange={(val) => {
                setUserData((state) => {
                  return {
                    ...state,
                    address: { ...state.address, line_1: val.target.value },
                  };
                });
              }}
            />
          </div>

          <div className={classes["custom-input-container"]}>
            <label htmlFor="create-address">Country</label>
            <Input
              type="address"
              placeholder="Enter address..."
              id="create-address"
              disabled={true}
              value={userData.address.country}
            />
          </div>

          <div className={classes["custom-input-container"]}>
            <label htmlFor="create-address">State</label>
            <select
              className={classes["custom-input-select"]}
              name="state"
              id="state"
              class="form-control"
              onChange={(val) =>
                setUserData((state) => {
                  return {
                    ...state,
                    address: { ...state.address, state: val.target.value },
                  };
                })
              }
            >
              <option value="Andhra Pradesh">Andhra Pradesh</option>
              <option value="Andaman and Nicobar Islands">
                Andaman and Nicobar Islands
              </option>
              <option value="Arunachal Pradesh">Arunachal Pradesh</option>
              <option value="Assam">Assam</option>
              <option value="Bihar">Bihar</option>
              <option value="Chandigarh">Chandigarh</option>
              <option value="Chhattisgarh">Chhattisgarh</option>
              <option value="Dadar and Nagar Haveli">
                Dadar and Nagar Haveli
              </option>
              <option value="Daman and Diu">Daman and Diu</option>
              <option value="Delhi">Delhi</option>
              <option value="Lakshadweep">Lakshadweep</option>
              <option value="Puducherry">Puducherry</option>
              <option value="Goa">Goa</option>
              <option value="Gujarat">Gujarat</option>
              <option value="Haryana">Haryana</option>
              <option value="Himachal Pradesh">Himachal Pradesh</option>
              <option value="Jammu and Kashmir">Jammu and Kashmir</option>
              <option value="Jharkhand">Jharkhand</option>
              <option value="Karnataka">Karnataka</option>
              <option value="Kerala">Kerala</option>
              <option value="Madhya Pradesh">Madhya Pradesh</option>
              <option value="Maharashtra">Maharashtra</option>
              <option value="Manipur">Manipur</option>
              <option value="Meghalaya">Meghalaya</option>
              <option value="Mizoram">Mizoram</option>
              <option value="Nagaland">Nagaland</option>
              <option value="Odisha">Odisha</option>
              <option value="Punjab">Punjab</option>
              <option value="Rajasthan">Rajasthan</option>
              <option value="Sikkim">Sikkim</option>
              <option value="Tamil Nadu">Tamil Nadu</option>
              <option value="Telangana">Telangana</option>
              <option value="Tripura">Tripura</option>
              <option value="Uttar Pradesh">Uttar Pradesh</option>
              <option value="Uttarakhand">Uttarakhand</option>
              <option value="West Bengal">West Bengal</option>
            </select>
          </div>

          <div className={classes["custom-input-container"]}>
            <label htmlFor="create-address">Pincode</label>
            <Input
              type="address"
              placeholder="Enter address..."
              id="create-address"
              maxLength={6}
              onChange={(val) =>
                setUserData((state) => {
                  return {
                    ...state,
                    address: { ...state.address, pincode: val.target.value },
                  };
                })
              }
            />
          </div>

          <div className={classes["custom-input-container"]}>
            <label htmlFor="create-phone-number">Phone Number</label>
            <Input
              type="tel"
              placeholder="Enter Phone..."
              id="create-phone-number"
              onChange={(val) => {
                if (Number.isFinite(+val)) {
                  setUserData((state) => {
                    return { ...state, phone: val.target.value };
                  });
                }
              }}
            />
          </div>

          <div className={classes["custom-input-container"]}>
            <label htmlFor="create-email">E-mail</label>
            <Input
              type="email"
              placeholder="Enter Email..."
              id="create-email"
              onChange={(val) =>
                setUserData((state) => {
                  return { ...state, email: val.target.value };
                })
              }
            />
          </div>

          <div className={classes["custom-input-container"]}>
            <label htmlFor="create-aadhaar">Aadhaar Number</label>
            <Input
              type="tel"
              placeholder="Enter Aadhaar..."
              id="create-aadhaar"
              maxLength={12}
              onChange={(val) => {
                if (Number.isFinite(+val)) {
                  setUserData((state) => {
                    return { ...state, aadhar: val };
                  });
                }
              }}
            />
          </div>
        </div>
        <Button title="Signup" onClick={submitHandler} />
      </form>
    </Card>
  );
}

export default Signup;
