import ParticlesComponent from '../Particles'
import React, { useState, useEffect } from 'react';
import '../../App.css'
import Logout from '../button/Logout'

export default function PassengerBill() {
    const [trips, setTrips] = useState([])

    useEffect(() => {
        const passenger_id = localStorage.getItem('email');
        console.log(passenger_id)
        const fetchTrips = async () => {
            const response = await fetch(`http://localhost:5000/getAllTrips?passenger_id=${passenger_id}`);
            const data = await response.json();
            setTrips(data);
        }
        fetchTrips();
    }, []);

    return (
        <div className='App-header'>
            <ParticlesComponent />
            <div className="title">
                <Logout />
                {trips.map((trip) => (
                    <div key={trip.trip_id}>
                        <br></br>
                        <label>Trip ID: {trip.trip_id}</label>
                        <br></br>
                        <label>Pickup location: {trip.pickup_location} </label>
                        <br></br>
                        <label>Dropoff location: {trip.dropoff_location} </label>
                        <br></br>
                        <label>Total cost (CAD): {(trip.distance * 1.25)}</label>
                        <br></br>
                        <label>Trip length (km): {trip.distance}</label>
                        <br></br>
                    </div>
                ))}
            </div>
        </div >
    );
}