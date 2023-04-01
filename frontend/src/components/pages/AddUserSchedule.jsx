import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import ParticlesComponent from '../Particles'
import ButtonCustom from '../button/Button'
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { notifyError, notifySuccess } from './Signup';

import '../../App.css'

var start_time = null;
var end_time = null;
var email = null;

export default function AddUserSchedule(){
 
start_time = React.useRef();
end_time = React.useRef();
email = React.useRef();
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
                    <label>Start Time</label><br/>
                    <input ref={start_time} type="text" id="start_time" name="start_time" required/><br/>
                    <br></br>
                </p>
                <p>
                    <label>End Time</label><br/>
                    <input ref={end_time} type="text" id="end_time" name="end_time" required/><br/>
                    <br></br>
                </p>
                <p>
                    <label>Enter your email</label><br/>
                    <input ref={email} type="email" id="email" name="email" required/><br/>
                    <br></br>
                </p>
                <p>
                 <ButtonCustom type="submit" style={{ height: "39px", width: "156px", fontSize: "20px" }} title="Submit" id="   "></ButtonCustom>
                </p>
                <ToastContainer />
            </form>
        </div>
    </div>
  )

}
async function post(event) {
    event.preventDefault();
    let response = await fetch('http://localhost:5000/addUserSchedule', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "email": email.current.value, "sched_start": start_time.current.value, "sched_end": end_time.current.value})
    })
    let result = await response.json();
    if (response.ok) {
        // Store the email in local storage
        alert(result.message);
        notifySuccess(result.message);

    } else {
        alert(result.message);
        notifyError(result.message);
    }
}