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
        document.getElementById("length").innerHTML = `Trip length (km): ${(tripDetails.distance)/1000} km`;
        document.getElementById("fuel").innerHTML = `Estimated fuel consumption (L/km): ${((tripDetails.distance)*0.07/1000).toFixed(5)}`;
        document.getElementById("c02").innerHTML = `Estimated C02 emission saved (approx. g of CO2): ${(2.5*(tripDetails.distance)*0.07*(tripDetails.num_passengers+1)).toFixed(5)} g`;
    }
    fetchTripDetails(trip_id).then((tripDetails) =>
        updateHTML(tripDetails)
    )

    function parseStringToNumber(inputString){
        const numberMatch = inputString.match(/[-+]?[0-9]*\.?[0-9]+/);
        const number = numberMatch ? parseFloat(numberMatch[0]) : NaN;

        return parseFloat(number.toFixed(4)); 
    }
    
    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="centered">
                <Link to="/display-trip"><p>Return to trip information</p></Link>
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <h2>Detailed Trip Cost</h2>
                <h3>Trip ID: {trip_id}</h3>
                <br></br>
                <br></br>
                <label id="cost">...</label>
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
