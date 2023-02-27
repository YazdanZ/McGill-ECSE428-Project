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
export default function Create_Trip()  {

    distance_km = React.useRef();



    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="title" style={{width: "500px", height:"200px", top:"70px", left:"100px"}}>
                <h1>Create Trip</h1>
                <form className='form'>
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
    let response = await fetch('http://localhost:5000/createTrip', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"vehicle_id":10, "passenger_id":"null", "distance_km":distance_km.current.value})
    })
    let result = await response.json();

    if (response.ok) {
        alert(result.message);

    }
    else {
        alert(result.message);
    }


}

