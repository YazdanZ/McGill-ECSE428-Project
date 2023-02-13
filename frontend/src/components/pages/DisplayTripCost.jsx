import React from 'react'
import { Link } from 'react-router-dom'
import ParticlesComponent from '../Particles'

import '../../App.css'

export default function DisplayTripCost() {
    
    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="centered">
                <a href="#">Return to trip information</a>
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <h2>Trip Cost</h2>
                <h3 id="trip-id">Trip ID: XXXXXX</h3>
                <br></br>
                <br></br>
                <label  id="price">Total cost (CAD): XX.XX</label>
                <br></br>
                <label  id="num_passengers">Num passengers: XX</label>
                <br></br>
                <label  id="price_pp">Cost per passenger (CAD): XX.XX</label>
                <br></br>
                <br></br>
                <label  id="trip_length">Trip length (km): XX.XX</label>
                <br></br>
                <label  id="fuel_cons">Estimated fuel consumption (L): XX.XX</label>
                <br></br>
                <label  id="emissions_saved">Estimated C02 emission saved (kg of CO2): XX.XX</label>
            </div>
        </div>
    )

}
