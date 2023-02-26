import React, { useState, useEffect } from 'react';
import ParticlesComponent from '../Particles'
import { Link } from 'react-router-dom';
import '../../App.css'

export default function TripDisplay() {
  //const passenger_id = "mark@mail.com"; //hardcoded value until create trip and user sessions are implemented
  //const trip_id = 1; //hardcoded trip_id
  const passenger_id = localStorage.getItem('email');
  console.log(passenger_id)
  const [tripDetails, setTripDetails] = useState({});

  useEffect(() => {
    const fetchTripDetails = async () => {
      const response = await fetch(`http://localhost:5000/getTrip?passenger_id=${passenger_id}`); //searches for the first trip assigned to the passenger
      //const response = await fetch(`http://localhost:5000/getTrip?trip_id=${trip_id}`); //passes a trip id to retrieve the trip
      const data = await response.json();
      console.log(data)
      setTripDetails(data);
    }
    fetchTripDetails();
  }, []);

  return (
    <div>
      <div className="trip-display" style={{position: "relative", zIndex: "1"}}>
        <div className="box" style={{width:"700px", height:"450px", border: "1px solid black", right:"575px", position:"absolute", top:"100px"}}></div>
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
              <strong>Cost:</strong> {tripDetails.cost}$
              <button style={{ backgroundColor: 'transparent', border: 'none', cursor: 'pointer' }}>
                <Link to={`/trip-cost?trip_id=${tripDetails.trip_id}`}>
                  <p>View Details</p>
                </Link>
              </button>
            </p>
          </form>
        </div>
      </div>
      <ParticlesComponent style={{position: "absolute", top: "0", left: "0", zIndex: "0"}}/>
    </div>
  );
};