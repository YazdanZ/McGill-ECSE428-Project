import React, { useState, useEffect } from 'react';
import ParticlesComponent from '../Particles'
import { Link } from 'react-router-dom';
import '../../App.css'

export default function TripDisplay() {
  const passengerId = 1; //hardcoded value until create trip and user sessions are implemented
  const [tripDetails, setTripDetails] = useState({});

  useEffect(() => {
    const fetchTripDetails = async () => {
      const response = await fetch(`/getTrip?passengerId=${passengerId}`);
      const data = await response.json();
      setTripDetails(data);
    }
    fetchTripDetails();
  }, []);

  return (
    <html>
      <head>
        <title>McPool Trip Display</title>
      </head>
      <body>
        <div className="trip-display" style={{position: "relative", zIndex: "1"}}>
          <div class="box" style={{width:"700px", height:"450px", border: "1px solid black", right:"575px", position:"absolute", top:"100px"}}></div>
          <h1 style={{color: "white", tab:"10", paddingTop: "40px"}}> MAP </h1>
          <h1 style={{ paddingTop: "510px" }}>Trip Details</h1>
          <div className="trip-details">
            <form style={{width: "500px"}} className='form'>
              <p><strong>Driver:</strong> {tripDetails.driver_name}</p>
              <p><strong>Vehicle:</strong> {tripDetails.driver_vehicle}</p>
              <p><strong>Pickup Location:</strong> {tripDetails.pickup_location}</p>
              <p><strong>Dropoff Location:</strong> {tripDetails.dropoff_location}</p>
              <p><strong>Distance:</strong> {tripDetails.distance} kilometers</p>
              <p><strong>Duration:</strong> {tripDetails.duration} minutes</p>
              <p>
                <strong>Cost:</strong> {tripDetails.cost} 
                <button style={{ backgroundColor: 'transparent', border: 'none', cursor: 'pointer' }}>
                  <Link to={`/trip-cost?trip_id=${tripDetails.tripId}`}>
                    <p>View Details</p>
                  </Link>
                </button>
              </p>
            </form>
          </div>
        </div>
        <ParticlesComponent style={{position: "absolute", top: "0", left: "0", zIndex: "0"}}/>
      </body>
    </html>
  );
};