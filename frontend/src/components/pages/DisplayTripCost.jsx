import React from 'react'
import { Link } from 'react-router-dom'
import ParticlesComponent from '../Particles'

import '../../App.css'

export default function DisplayTripCost() {
    const fetchTripDetails = async (trip_id) => {
        const response = await fetch(`http://localhost:5000/getTrip?trip_id=${trip_id}`);
        const data = await response.json();
        return data;
      }
    const urlParams = new URLSearchParams(window.location.search);
    const trip_id = urlParams.get('trip_id');
    const tripDetails = fetchTripDetails(trip_id);
    
    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="centered">
                <Link to="/display-trip" className="return_link"><p>Return to trip information</p></Link>
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <h2>Detailed Trip Cost</h2>
                <h3 id="tripid">Trip ID: {trip_id}</h3>
                <br></br>
                <br></br>
                <label id="cost">Total cost (CAD): {tripDetails.cost}</label>
                <br></br>
                <label id="passengers">Num passengers: {tripDetails.num_passengers}</label>
                <br></br>
                <label id="seats">Available Seats: {tripDetails.num_seats-tripDetails.num_passengers}</label>
                <br></br>
                <label id="costpp">Cost per passenger (CAD): {tripDetails.cost/(tripDetails.num_passengers+1)}</label>
                <br></br>
                <label id="length">Trip length (km): {tripDetails.distance}</label>
                <br></br>
                <label id="fuel">Estimated fuel consumption (L/km): {tripDetails.fuel_consumption}</label>
                <br></br>
                <label id="c02">Estimated C02 emission saved (approx. kg of CO2): {2.5*tripDetails.distance*tripDetails.fuel_consumption*tripDetails.num_passengers}</label>
            </div>
        </div>
    )
}
