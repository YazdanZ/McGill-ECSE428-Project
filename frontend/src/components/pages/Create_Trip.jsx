import React from 'react'
import ParticlesComponent from '../Particles'
//import '../../App.css'
import ButtonCustom from '../button/Button'
import { Link } from 'react-router-dom'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import LoginInfo from '../pages/Login'


export const notifySuccess = (text) => toast.success(text, {
    containerId: "c1",
    position: "bottom-right",
    hideProgressBar: false,
    closeOnClick: true,
    pauseOnHover: true,
    draggable: false,
    progress: undefined,
    theme: "light",
});

export const notifyError = (text) => toast.error(text, {
    containerId: "c2",
    position: "bottom-right",
    hideProgressBar: false,
    closeOnClick: true,
    pauseOnHover: true,
    draggable: false,
    progress: undefined,
    theme: "light",
});



var distance_km = null;
var pick_up_address_line_1 = null;
var pick_up_city = null;
var pick_up_postal_code = null;
var drop_off_address_line_1 = null;
var drop_off_city = null;
var drop_off_postal_code = null;

export default function Create_Trip()  {

    distance_km = React.useRef();
    pick_up_address_line_1 = React.useRef();
    pick_up_city = React.useRef();
    pick_up_postal_code = React.useRef();
    drop_off_address_line_1 = React.useRef();
    drop_off_city = React.useRef();
    drop_off_postal_code = React.useRef();





    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="title" style={{width: "500px", height:"200px", top:"10px", left:"100px"}}>
                <h1>Create Trip</h1>
                <form className='form'>
                     <p>
                        <label>Pick Up Address Line 1</label><br/>
                        <input ref={pick_up_address_line_1} type="text" id="pick_up_address_line_1" name="pick_up_address_line_1" required /><br/>
                        <label></label><br/>
                    </p>
                     <p>
                        <label>Pick Up City</label><br/>
                        <input ref={pick_up_city} type="text" id="pick_up_city" name="pick_up_city" required /><br/>
                        <label></label><br/>
                    </p>
                     <p>
                        <label>Pick Up Postal Code</label><br/>
                        <input ref={pick_up_postal_code} type="text" id="pick_up_postal_code" name="pick_up_postal_code" required /><br/>
                        <label></label><br/>
                    </p>
                        <p>
                        <label>Drop Off Address Line 1</label><br/>
                        <input ref={drop_off_address_line_1} type="text" id="drop_off_address_line_1" name="drop_off_address_line_1" required /><br/>
                        <label></label><br/>
                    </p>
                     <p>
                        <label>Drop Off City</label><br/>
                        <input ref={drop_off_city} type="text" id="drop_off_city" name="drop_off_city" required /><br/>
                        <label></label><br/>
                    </p>
                     <p>
                        <label>Drop Off Postal Code</label><br/>
                        <input ref={drop_off_postal_code} type="text" id="drop_off_postal_code" name="drop_off_postal_code" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>Total Distance to Travel</label><br/>
                        <input ref={distance_km} type="text" id="distance_km" name="distance_km" required /><br/>
                        <label></label><br/>
                    </p>

                    <p>
                     <Link to="/user-info">
                        <ButtonCustom onClick={post1} style={{ height: "39px", width: "156px", fontSize: "20px" }} title="Submit" id="sub_btn" type="button"></ButtonCustom>
                     </Link>
                    </p>
                    <ToastContainer/>
                </form>

            </div>
            <div class="box" style={{width:"700px", height:"500px", border: "1px solid black", right:"130px", position:"absolute", top:"100px"}}></div>
                        <br/><br/><br/><br/><br/>
                        <h1 style={{color: "white", tab:"10"}}> MAP </h1>
        </div>
    )

}

async function post1(event) {
    event.preventDefault();

     let response3 = await fetch('http://localhost:5000/createPickUp', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"city":pick_up_city.current.value, "address_line_1":pick_up_address_line_1.current.value, "postal_code":pick_up_postal_code.current.value})
    })
    let result3 = await response3.json();
    if(response3.ok){

    }
    else{
        alert(result3.message);
    }





     let response2 = await fetch('http://localhost:5000/createDropOff', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"city":drop_off_city.current.value, "address_line_1":drop_off_address_line_1.current.value, "postal_code":drop_off_postal_code.current.value})
    })

    let result2 = await response2.json();
    if(response2.ok){

    }
    else{
        alert(result2.message);
    }





    let response = await fetch('http://localhost:5000/createTrip', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"vehicle_id":12, "passenger_id":"null", "distance_km":distance_km.current.value, "drop_off_address_id":result2.address_id, "pick_up_address_id":result3.address_id})
    })
    let result = await response.json();
    alert(result.message);





}

