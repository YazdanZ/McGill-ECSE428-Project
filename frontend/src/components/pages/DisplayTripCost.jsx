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
    const updateHTML = (tripDetails) => {
        document.getElementById("cost").innerHTML = `Total cost (CAD): ${tripDetails.cost}`;
        document.getElementById("passengers").innerHTML = `Num passengers: ${tripDetails.num_passengers}`;
        document.getElementById("seats").innerHTML = `Available Seats: ${tripDetails.num_seats-tripDetails.num_passengers}`;
        document.getElementById("costpp").innerHTML = `Cost per passenger (CAD): ${tripDetails.cost/(tripDetails.num_passengers+1)}`;
        document.getElementById("length").innerHTML = `Trip length (km): ${tripDetails.distance}`;
        document.getElementById("fuel").innerHTML = `Estimated fuel consumption (L/km): ${tripDetails.fuel_consumption}`;
        document.getElementById("c02").innerHTML = `Estimated C02 emission saved (approx. kg of CO2): ${2.5*tripDetails.distance*tripDetails.fuel_consumption*tripDetails.num_passengers}`;
    }
    fetchTripDetails(trip_id).then((tripDetails) =>
        updateHTML(tripDetails)
    )
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
                <label id="cost"></label>
                <br></br>
                <label id="passengers">Num passengers: ...</label>
                <br></br>
                <label id="seats">Available Seats: ...</label>
                <br></br>
                <label id="costpp">Cost per passenger (CAD): ...</label>
                <br></br>
                <label id="length">Trip length (km): ...</label>
                <br></br>
                <label id="fuel">Estimated fuel consumption (L/km): ...</label>
                <br></br>
                <label id="c02">Estimated C02 emission saved (approx. kg of CO2): ...</label>
            </div>
        </div>
    )
}
