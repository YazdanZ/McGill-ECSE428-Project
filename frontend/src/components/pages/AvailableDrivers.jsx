import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import ParticlesComponent from '../Particles'
import ButtonCustom from '../button/Button'
import { notifyError, notifySuccess } from './Signup';

import '../../App.css'

var email = null
var trip_id_ref = null

export default function AvailableDrivers() {
    email = React.useRef()
    trip_id_ref = React.useRef()
    const [trips, getAvailTrips] = useState([]);

    useEffect(() => {
        const fetchTrips = async()=> {
            const response = await fetch(`http://localhost:5000/getAvailableTrips/`);
            const data = await response.json();
            console.log(data);
            getAvailTrips(data);
            
            return data;
        };
        fetchTrips();
    }, []);
    async function post(event) {
        event.preventDefault();
        let response = await fetch('http://localhost:5000/assignPassenger/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ "email": email.current.value, "trip_id": trip_id_ref.current})
        })
        let result = await response.json();
        if (response.ok) {
            notifySuccess(result.message);
        } else {
            notifyError(result.message);
        }
    }
    
    
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
                <form className='form' onSubmit={post}>
                {trips.map((trip) => (
                <div key={trip.trip_id}>
                 
                 <br></br>
                 <label ref={ref=> trip_id_ref.current = trip.trip_id}>Trip {trip.trip_id}</label>
                 <br></br>
                 
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
                <br></br>
                
                <label>Pick this trip</label>
                <br></br>
                <label>Enter your email:</label><br />
                        <input ref={email} type="email" name="email" required /><br />
                        <label></label><br />
                        <p>
                        <ButtonCustom type="submit" style={{ height: "39px", width: "156px", fontSize: "20px" }} title="Submit" id="sub_btn"></ButtonCustom>
                    </p>
                
                </div>
                ))}
                </form>
            </div>
        </div>
    )
}


