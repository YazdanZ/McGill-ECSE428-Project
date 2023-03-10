import React from 'react'
import ParticlesComponent from '../Particles'
import '../../App.css'
import ButtonCustom from '../button/Button'
import Map from '../Map'


export default function Create_Trip()  {


    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="title" style={{width: "500px", height:"200px", top:"70px", left:"100px"}}>
                <h1>Create Trip</h1>
                <form className='form'>
                    <p>
                        <label>Available Seats</label><br/>
                        <input type="text" name="available_seats" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>Total Trip Fuel Consumption (KM/Liter)</label><br/>
                        <input type="text" name="fuel_consumption" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>Total Trip Distance Covered</label><br/>
                        <input type="text" name="distance_km" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>Pickup Location</label><br/>
                        <input type='text' name="pickup_location" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>Drop-Off Location</label><br/>
                        <input type="text" name="dropoff_location" required /><br/>
                        <label></label><br/>
                    </p>

                    <p>
                        <ButtonCustom onClick={post1} style={{ height: "39px", width: "156px", fontSize: "20px" }} title="Submit" id="sub_btn" type="button"></ButtonCustom>
                    </p>
                </form>

            </div>
            <div class="box" style={{width:"700px", height:"500px", border: "1px solid black", right:"130px", position:"absolute", top:"100px"}}>
                <Map/>
            </div>
                        
        </div>
    
    )

}

function post1() {

    let form = document.querySelector("form");

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        let formdata = new FormData(this);
        let vehicle_id =1;
        let passenger_id="mihiranshul@gmail.com";
        let distance_km = formdata.get("distance_km");


        e.preventDefault();
        fetch('http://localhost:5000/createTip', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({"vehicle_id":vehicle_id, "passenger_id": passenger_id,  "distance_km": distance_km})
        })
            .then(response => alert("New Driver Trip created"))
        e.preventDefault();
    });
}

