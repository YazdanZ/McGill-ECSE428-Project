import React from 'react';
import ParticlesComponent from '../Particles'
import { Link } from 'react-router-dom';
import Logout from '../button/Logout';

import '../../App.css'

export default function TripDisplay() {
  return (
    <html>
      <ParticlesComponent />
      <head>
        <title>McPool Trip Display</title>
      </head>
      <body>
        <div className="trip-display">
          <Logout />
          <div class="box" style={{ width: "700px", height: "450px", border: "1px solid black", right: "575px", position: "absolute", top: "100px" }}></div>
          <h1 style={{ color: "white", tab: "10", paddingTop: "40px" }}> MAP </h1>

          <h1 style={{ paddingTop: "510px" }}>Trip Details</h1>
          <div className="trip-details">
            <form style={{ width: "500px" }} className='form'>
              <p><strong>Driver:</strong> Andrew Chirita</p>
              <p><strong>Vehicle:</strong> Toyota Corolla</p>
              <p><strong>Pickup Location:</strong> 542 Sherbrooke Street</p>
              <p><strong>Dropoff Location:</strong> 341 University Street</p>
              <p><strong>Distance:</strong> 5 kilometers</p>
              <p><strong>Duration:</strong> 5 minutes</p>
              <p><strong>Cost:</strong> $20.00</p>
            </form>
          </div>
        </div>
      </body>
    </html>
  );
};