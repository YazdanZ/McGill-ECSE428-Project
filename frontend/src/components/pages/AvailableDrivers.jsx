import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import ParticlesComponent from '../Particles'

import '../../App.css'

export default function AvailableDrivers() {
    const [trips, getAvailTrips] = useState([]);

    useEffect(() => {
        const fetchTrips = async()=> {
            const response = await fetch(`http://localhost:5000/getAvailableTrips/`);
            const data = await response.json();
            getAvailTrips(data);
        };
        fetchTrips();
    }, []);
    
    
    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="centered">
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <h2>Available trips</h2>
                <br></br>
                <br></br>
                {trips.map((trip) => (
                <div key={trip.trip_id}>
                 <label>Number of seats: {trip.available_seats}</label>
                 <br></br>
                <label>Distance in km: {trip.distance_km}</label>
                <br></br>
                <label>Driver's name: {trip.driver_name}</label>
                <br></br>
                <label>Drop off address: {trip.drop_off_address}</label>
                <br></br>
                <label>Fuel consumption: {trip.fuel_consumption}</label>
                <br></br>
                <label>Pick up address: {trip.pick_up_address}</label>
                <br></br>
                <label>Vehicle type: {trip.vehicle_name}</label>
                </div>
                ))}
            </div>
        </div>
    )
}
