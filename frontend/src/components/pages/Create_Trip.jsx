import React from 'react'
import ParticlesComponent from '../Particles'
//import '../../App.css'
import ButtonCustom from '../button/Button'


export default function Create_Trip()  {


    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="title" style={{width: "20vw", height:"70vh", top:"0", left:"10vw"}}>
                <h1>Create Trip</h1>
                <form className='form'>
                    <p>
                        <label>Available Seats</label><br/>
                        <input type="text" name="available_seats" style={{ boxShadow: '2px 2px 5px #888888' }} required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>Pickup Location</label><br/>
                        <input type='text' name="pickup_location" style={{ boxShadow: '2px 2px 5px #888888' }} required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>Drop-Off Location</label><br/>
                        <input type="text" name="dropoff_location" style={{ boxShadow: '2px 2px 5px #888888' }} required /><br/>
                        <label></label><br/>
                    </p>

                    <p>
                        <ButtonCustom onClick={post2} style={{ height: "39px", width: "156px", fontSize: "14px" , margin:"15px"}} title="Calculate Distance" id="sub_btn" type="button"></ButtonCustom>
                          </p>

                    <p>
                        <label >Total Trip Distance Covered</label><br/>
                        <label id="distance_text" style={{ color: '#6a6868' }}>NaN</label><br/>
                        <label></label><br/>
                    </p>

                    <p>
                        <label >Total Fuel Consumption (KM/Liter)</label><br/>
                        <label id="fuel_text" style={{ color: '#6a6868' }}>NaN</label><br/>
                        <label></label><br/>
                    </p>
                    
                    

                    <p>
                        <ButtonCustom onClick={post1} style={{ height: "39px", width: "156px", fontSize: "20px" }} title="Submit" id="sub_btn" type="button"></ButtonCustom>
                    </p>
                </form>

            </div>
            <div className="box" style={{width:"700px", height:"500px", border: "1px solid black", right:"130px", position:"absolute", top:"100px"}}></div>
                        <br/><br/><br/><br/><br/>
                        <h1 style={{color: "white", tab:"10"}}> MAP </h1>
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
function post2() {
  let form = document.querySelector("form");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    let formdata = new FormData(this);
    let passenger_id="andrew@mail.com";
    let pickup_location = formdata.get("pickup_location");
    let dropoff_location = formdata.get("dropoff_location");

    e.preventDefault();
    fetch('http://localhost:5000/calculateDistance', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({"userEmail":passenger_id , "pickupLocation": pickup_location,  "dropoffLocation": dropoff_location})
    })
    .then(response => response.json())
    .then(data => {
      let distance = data.distance;
      let distanceText = document.getElementById("distance_text");
      distanceText.textContent = distance.toString();

      //this value is an approximation and we'll come up with a better way to calculating this in Sprint B
      let fuelConsumption= distance/10;
      let fuelConsumptionText = document.getElementById("fuel_text");
      fuelConsumptionText.textContent = fuelConsumption.toString();
    })
  });
}
