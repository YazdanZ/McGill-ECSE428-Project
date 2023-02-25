import React from 'react'
import ParticlesComponent from '../Particles'
import Logout from '../button/Logout'

import '../../App.css'

const drivers = ['Driver 1', 'Driver 2', 'Driver 3', 'Driver 4', 'Driver 5'];

const DriverList = ({ drivers, handleClick }) => {
  return drivers.map((driver, index) => (
    <li key={driver}>
      {driver}
      <button className="driver-buttons" id={`driver-button-${driver}`} onClick={() => handleClick(driver)}>Pick Driver</button>
    </li>
  ));
};

export default function AvailableDrivers() {
  const handleClick = (driver) => {
    let allDrivers = document.getElementsByClassName("driver-buttons");
    for(let driver of allDrivers){
      driver.textContent= "Pick Driver";
    }
    let driverButtonList = document.getElementById(`driver-button-${driver}` );
    driverButtonList.textContent="Selected";
  };

  //to not refresh the page when a button is pressed
const handleSubmit = (event) => {
    event.preventDefault(); // prevent the default form submission behavior
  };

  return (
    <div className='App-header'>
      <ParticlesComponent />
      <div className="title">
        <Logout />
        <h2>Available Drivers</h2>
        <form className='form' onSubmit={handleSubmit}>
          <div id="listDrivers">
            <ul>
              <DriverList drivers={drivers} handleClick={handleClick} />
            </ul>

          </div>
        </form>

      </div>
    </div>
  )

}
