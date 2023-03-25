import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import ParticlesComponent from '../Particles'
import ButtonCustom from '../button/Button'
import { notifyError, notifySuccess } from './Signup';

import '../../App.css'

export default function AddDriverSchedule(){
 return(
    <div className='App-header'>
        <ParticlesComponent/>
        <div className="centered">
            <br></br>
            <br></br>
            <h2>Add your schedules</h2>
            <br></br>
            <br></br>
            <form className='form'>
                <p>
                    <label>Trip to McGill</label>
                    <br></br>
                    <label>Departure Time</label><br/>
                    <input type="text" id="Departure_to_mcgill" name="Departure_to_mcgill" required/><br/>
                    <br></br>
                    <label>Arrival Time</label><br />
                    <input type="text" id="Arrival_to_mcgill" name="arrival_to_mcgill" required/> <br/>
                    <br></br>
                </p>
                <p>
                   <label>Trip from McGill</label>
                    <br></br>
                    <label>Departure Time</label><br/>
                    <input type="text" id="Departure_from_mcgill" name="Departure_from_mcgill" required/><br/>
                    <br></br>
                    <label>Arrival Time</label><br/>
                    <input type="text" id="Arrival_from_mcgill" name="arrival_from_mcgill" required/><br/>
                    <br></br>
            
                </p>
                <p>
                  <ButtonCustom style={{ height: "39px", width: "156px", fontSize: "20px" }} title="Add schedule" id="sub_btn" type="button"></ButtonCustom>
                </p>

            </form>
        </div>
    </div>
  )

}