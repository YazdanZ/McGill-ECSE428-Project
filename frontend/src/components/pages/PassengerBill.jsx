import React from 'react'
import ParticlesComponent from '../Particles'
import '../../App.css'
import Logout from '../button/Logout'

export default function PassengerBill() {
    const bills = [];

    for (let i = 0; i < 5; i++) {
        bills.push(
            <div key={i}>
                <br></br>
                <label>Trip ID:</label>
                <br></br>
                <label>Total cost (CAD): </label>
                <br></br>
                <label>Trip length (km): </label>
                <br></br>
            </div>
        );
    }

    return (
        <div className="App-header">
            <ParticlesComponent />
            <div className="centered">
                <Logout />
                <br></br>
                <h2>All previous bills</h2>
                {bills}
            </div>
        </div>
    );
}
