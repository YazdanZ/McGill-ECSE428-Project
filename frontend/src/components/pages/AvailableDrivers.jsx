import React from 'react'
import { Link } from 'react-router-dom'
import ParticlesComponent from '../Particles'

import '../../App.css'

const drivers = ['Driver 1', 'Driver 2', 'Driver 3', 'Driver 4', 'Driver 5'];

const DriverList = ({ drivers, handleClick }) => {
    return drivers.map((driver) => (
      <li key={driver}>
        {driver}
        <button onClick={() => handleClick(driver)}>Pick Driver</button>
      </li>
    ));
  };

export default function AvailableDrivers() {
    const handleClick = (driver) => {
        console.log(`Driver ${driver} selected`);
      };

    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="title">
                <h2>Available Drivers</h2>
                <form className='form'>
                  <div id="listDrivers">
                      <ul style={{listStyleType: 'none'}}>
                        <DriverList drivers={drivers} />
                      </ul>

                    </div> 
                </form>
                
            </div>
        </div>
    )

}