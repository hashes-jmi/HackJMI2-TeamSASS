import React, { Fragment, useEffect } from "react";
import { Map, InfoWindow, Marker, GoogleApiWrapper } from "google-maps-react";
const MapContainer = (props) => {
  const mapStyles = {
    width: "100%",
    height: "100%",
  };

  return (
    <Fragment>
      <Map google={props.google} zoom={14} style={mapStyles}>
        <Marker name={"Current location"} />
      </Map>
    </Fragment>
  );
};

export default GoogleApiWrapper({
  apiKey: "AIzaSyC-64vsIVad3WwPFX1sxqbHucAmtgR7Kms",
})(MapContainer);
