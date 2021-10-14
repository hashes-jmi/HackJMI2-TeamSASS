import React, { Fragment } from "react";
import Button from "../UI/Buttons/Button";
import Card from "../UI/Card/Card";
import classes from "./Home.module.css";
import pmPic from "../../images/pmPic.png";
import Colors from "../Colors";
import map from "../../images/map.png";
import Heading from "./../UI/Heading/Heading";

const servicesCardData = [
  {
    id: "c1",
    text: "Get your e-medical card",
    imgURL: "",
  },
  {
    id: "c2",
    text: "Watch live local or global health status",
    imgURL: "",
  },
  {
    id: "c3",
    text: "Get 25% discount on all health procedures with e-Medcard",
    imgURL: "",
  },
];

const Home = () => {
  return (
    <div className={classes["home-container"]}>
      <div className={classes.sidebar}>
        <div className={classes.mission}>
          <img src={pmPic} alt="PM of India, Mr.Modi" />
          <div>
            <p>PM DIGITAL HEALTH MISSION</p>
          </div>
        </div>
      </div>
      <main className={classes.content}>
        <Card>
          <section className={classes.intro}>
            <Heading text="NAME OF OUR WEBSITE" />
            <p>
              In order to achieve the mission
              of.....adkshadkjhaskdhaskdhaksdhkasdhkasdhvnhguta
              dhfh f bhgtuh ghuth dbgeht bghuthha bghus lorem epsum here and
              there and you and there my fine done compelte here and thenre but
              this is a compelte website to be publihsed online.
            </p>

            <Button title="Download Your e-MedCard" />
          </section>
        </Card>

        {/* SERVICES SECTION */}
        <Card>
          <section className={classes.services}>
            <Heading text="Our Services" />
            <div className={classes.display}>
              {/* SERVICES */}
              {servicesCardData.map((data) => (
                <div className={classes["service-card"]}>
                  <div className={classes["service-card--text"]}>HELLO</div>
                </div>
              ))}
            </div>
          </section>
        </Card>
      </main>
    </div>
  );
};

export default Home;
