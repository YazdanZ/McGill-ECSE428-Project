import React from 'react';
import { Link } from 'react-router-dom';

import '../../trip-display.css'

export default function TripDisplay() {
  return (
    <html>
      <head>
        <title>McPool Trip Display</title>
        <link rel="stylesheet" type="text/css" href="trip-display.css" />
        <script type="text/javascript" src="trip-display.js"></script>
      </head>
      <body>
        <header>
          <nav>
            <ul>
              <li><a href="#">Home</a></li>
            </ul>
          </nav>
        </header>
        <div className="trip-display">
          <h1>Trip Details</h1>
          <div className="trip-details">
            <p><strong>Driver:</strong> Andrew Chirita</p>
            <p><strong>Vehicle:</strong> Toyota Corolla</p>
            <p><strong>Pickup Location:</strong> 542 Sherbrooke Street</p>
            <p><strong>Dropoff Location:</strong> 341 University Street</p>
            <p><strong>Distance:</strong> 5 kilometers</p>
            <p><strong>Duration:</strong> 5 minutes</p>
            <p><strong>Cost:</strong> $20.00 <a href="trip-cost.html">See Details</a></p>
          </div>
        </div>
      </body>
    </html>
  );
};