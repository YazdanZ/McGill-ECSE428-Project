import React from 'react'
import { useState } from 'react';
import ParticlesComponent from '../Particles'
import '../../App.css'
import ButtonCustom from '../button/Button'
import MapForCreateTrip from '../MapForCreateTrip';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


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

    const [selectedPickup, setPickup] = useState("------");
    const [selectedDropoff, setDropoff] = useState("------");
    const [isLoading, setLoading] = useState(true);
    const [addresses, setAddresses] = useState([]);

    const fetchAddresses = async (passenger_id) => {
        const response = await fetch(`http://localhost:5000/getAddresses?passenger_id=${passenger_id}`);
        const data = await response.json();
        return data;
    }
    const urlParams = new URLSearchParams(window.location.search);
    const passenger_id = urlParams.get('passenger_id');
    if (isLoading) {
        fetchAddresses(passenger_id).then(data => {
            setAddresses(data);
            setLoading(false);
        });
    }

    function handlePickupChange(event) {
        setPickup(event.target.value);
        ;
    }
    function handleDropoffChange(event) {
        setDropoff(event.target.value);
    }

    async function post1(event) {
        event.preventDefault();
    
        if (distance_km.current.value.length === 0) {
            alert("Set a total distance.");
            return;
        }
        var result2 = {'address_id':0}
        var result3 = {'address_id':0}

        if (selectedDropoff === "Create New") {
            let response3 = await fetch('http://localhost:5000/createPickUp', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({"city":pick_up_city.current.value, "address_line_1":pick_up_address_line_1.current.value, "postal_code":pick_up_postal_code.current.value})
            })
            result3 = await response3.json();
            if(response3.ok){
    
            }
            else{
                alert(result3.message);
                return;
            }
        } else if (selectedDropoff === "------") {
            alert("Select a dropoff location.");
            return;
        } else if (selectedDropoff === selectedPickup) {
            alert("Pickup and dropoff address must be different.");
            return;
        } else {
            result3 = {'address_id':selectedDropoff}
        }
    
        if (selectedPickup === "Create New") {
            let response2 = await fetch('http://localhost:5000/createDropOff', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({"city":drop_off_city.current.value, "address_line_1":drop_off_address_line_1.current.value, "postal_code":drop_off_postal_code.current.value})
            })
    
            result2 = await response2.json();
            if(response2.ok){
    
            }
            else{
                alert(result2.message);
                return;
            }
        } else if (selectedPickup === "------") {
            alert("Select a pickup location.");
            return;
        } else {
            result2 = {'address_id':selectedPickup}
        }
        let response = await fetch('http://localhost:5000/createTrip', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({"vehicle_id":7, "passenger_id":passenger_id, "distance_km":distance_km.current.value, "drop_off_address_id":result2.address_id, "pick_up_address_id":result3.address_id})
        })
        let result = await response.json();
        alert(result.message);
    
    }
    if (isLoading) {
        return <div className="App">Loading...</div>;
    }
    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="title" style={{width: "70%", height:"10%", top:"-20px", left:"15%"}}>
                <h1>Create Trip</h1>
                <div style={{ display: 'flex' }}>
                    <div style={{ width: '50%', textAlign:"left" }}>
                    <label style={{height:"2px", margin:"0px"}}>Pick Up Address:</label>
                    <select value={selectedPickup} onChange={handlePickupChange} id='pickupDropdown'>
                        <option key={'------'} value={'------'}>------</option>
                        <option id={'create_new_pickup'} key={'Create New'} value={'Create New'}>Create New</option>
                        {addresses.map((address) => (
                        <option key={address.id} value={address.id}>{address.address}</option>
                        ))}
                    </select><br/>
                    {selectedPickup === 'Create New' && (
                        <div>
                        <form className='form'>
                            <p>
                                <label >Pick Up Address Line 1</label>
                                <input  ref={pick_up_address_line_1} type="text" id="pick_up_address_line_1" name="pick_up_address_line_1" required /><br/>
                                <label></label><br/>
                            </p>
                            <p>
                                <label >Pick Up City</label>
                                <input  ref={pick_up_city} type="text" id="pick_up_city" name="pick_up_city" required /><br/>
                                <label></label><br/>
                            </p>
                            <p>
                                <label >Pick Up Postal Code</label>
                                <input  ref={pick_up_postal_code} type="text" id="pick_up_postal_code" name="pick_up_postal_code" required /><br/>
                                <label></label><br/>
                            </p>
                        </form>
                        </div>
                    )}
                    <label style={{height:"2px", margin:"0px"}}>Dropoff Address:</label>
                    <select value={selectedDropoff} onChange={handleDropoffChange} id='dropoffDropdown'>
                        <option key={'------'} value={'------'}>------</option>
                        <option id={'create_new_dropoff'} key={'Create New'} value={'Create New'}>Create New</option>
                        {addresses.map((address) => (
                        <option key={address.id} value={address.id}>{address.address}</option>
                        ))}
                    </select><br/>
                    {selectedDropoff === 'Create New' && (
                        <div>
                        <form className='form'>
                                <p>
                                <label >Drop Off Address Line 1</label>
                                <input  ref={drop_off_address_line_1} type="text" id="drop_off_address_line_1" name="drop_off_address_line_1" required /><br/>
                                <label></label><br/>
                            </p>
                            <p>
                                <label >Drop Off City</label>
                                <input  ref={drop_off_city} type="text" id="drop_off_city" name="drop_off_city" required /><br/>
                                <label></label><br/>
                            </p>
                            <p>
                                <label >Drop Off Postal Code</label>
                                <input  ref={drop_off_postal_code} type="text" id="drop_off_postal_code" name="drop_off_postal_code" required /><br/>
                                <label></label><br/>
                            </p>
                        </form>
                        </div>
                    )}
                <div style={{ display: 'flex', justifyContent: 'end' }}>
                    <p>
                        <label>Total Distance to Travel      </label>
                        <input ref={distance_km} style ={{height: "30px", width: "100px"}} type="text" id="distance_km" name="distance_km" required /><br/>
                        <label></label><br/>
                    </p>
                
                <p>
                    <ButtonCustom onClick={post1} style={{ height: "39px", width: "156px", fontSize: "20px",marginLeft:"50px" }} title="Submit" id="sub_btn" type="button"></ButtonCustom>
                </p>
                
                    </div>
                </div>
                </div>
                <ToastContainer/>

            </div>
            <div class="box" style={{width:"600px", height:"500px", border: "1px solid black", right:"30px", position:"absolute", top:"105px"}}>
                <MapForCreateTrip selectedPickup={selectedPickup} setPickup={setPickup} selectedDropoff={selectedDropoff} setDropoff={setDropoff} isLoading={isLoading} setLoading={setLoading} addresses={addresses} setAddresses={setAddresses} pick_up_address_line_1={pick_up_address_line_1} pick_up_city={pick_up_city} pick_up_postal_code={pick_up_postal_code} drop_off_address_line_1={drop_off_address_line_1} drop_off_city={drop_off_city} drop_off_postal_code={drop_off_postal_code} distance_km={distance_km} />
            </div>


        </div>
    
    )

}