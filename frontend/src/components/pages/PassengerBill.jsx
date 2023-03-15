import React from 'react'
import ParticlesComponent from '../Particles'
import '../../App.css'
import Logout from '../button/Logout'

export default function PassengerBill() {
    return (
        <div className='App-header'>
            <ParticlesComponent />
            <div className="centered">
                <Logout />
                <br></br>
                <br></br>
                <br></br>
                <h2>All previous bills</h2>
                <br></br>
                <label>Trip ID:</label>
                <br></br>
                <label>Total cost (CAD): </label>
                <br></br>
                <label>Trip length (km): </label>
                <br></br>
                {billDisplay}
            </div>
        </div>
    )
}

function billDisplay() {
    var text = "";
    for (var i = 0; i < 5; i++) {
        text += "<h2>All previous bills</h2> <br></br> <label>Trip ID:</label> <br></br> <label>Total cost (CAD): </label> <br></br> <label>Trip length (km): </label> <br></br>";
    }
    return text;
}