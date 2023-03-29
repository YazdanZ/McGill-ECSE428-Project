import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import ParticlesComponent from '../Particles'
import ButtonCustom from '../button/Button'
import { notifyError, notifySuccess } from './Signup';

import '../../App.css'

// export const notifySuccess = (text) => toast.success(text, {
//     containerId: "c1",
//     position: "bottom-right",
//     hideProgressBar: false,
//     closeOnClick: true,
//     pauseOnHover: true,
//     draggable: false,
//     progress: undefined,
//     theme: "light",
// });

// export const notifyError = (text) => toast.error(text, {
//     containerId: "c2",
//     position: "bottom-right",
//     hideProgressBar: false,
//     closeOnClick: true,
//     pauseOnHover: true,
//     draggable: false,
//     progress: undefined,
//     theme: "light",
// });

var start_date = null;
var start_time = null;
var trip_id = null;

export default function AddDriverSchedule(){
 
 start_date = React.useRef();
 start_time = React.useRef();
 trip_id = React.useRef();
 return(
    <div className='App-header'>
        <ParticlesComponent/>
        <div className="centered">
            <br></br>
            <br></br>
            <h2>Add your schedules</h2>
            <br></br>
            <br></br>
            <form className='form' onSubmit={post}>
                <p>
                    <label>Start Date</label><br/>
                    <input ref={start_date} type="text" id="start_date" name="start_date" required/><br/>
                    <br></br>
                </p>
                <p>
                    <label>Start Time</label><br/>
                    <input ref={start_time} type="text" id="start_time" name="start_time" required/><br/>
                    <br></br>
                </p>
                <p>
                    <label>Enter Trip Id</label><br/>
                    <input ref={trip_id} type="text" id="trip_id" name="trip_id" required/><br/>
                    <br></br>
                </p>
                <p>
                 <ButtonCustom type="submit" style={{ height: "39px", width: "156px", fontSize: "20px" }} title="Submit" id="sub_btn"></ButtonCustom>
                </p>

            </form>
        </div>
    </div>
  )

}
async function post(event) {
    event.preventDefault();
    let response = await fetch('http://localhost:5000/addDriverSchedule', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "trip_id": trip_id.current.value, "start_date": start_date.current.value, "start_time": start_time.current.value})
    })
    let result = await response.json();
    if (response.ok) {
        notifySuccess(result.message);
    } else {
        notifyError(result.message);
    }
}