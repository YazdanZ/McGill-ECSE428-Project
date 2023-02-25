import React from 'react'
import ParticlesComponent from '../Particles'
import '../../styles.scss'
import ButtonCustom from '../button/Button'
import { Link } from 'react-router-dom'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


export const notifySuccess = (text) => toast.success(text, {
    position: "bottom-right",
    autoClose: 2000,
    hideProgressBar: false,
    closeOnClick: true,
    pauseOnHover: true,
    draggable: false,
    progress: undefined,
    theme: "light",
});

export const notifyError = (text) => toast.error(text, {
    position: "bottom-right",
    autoClose: 2000,
    hideProgressBar: false,
    closeOnClick: true,
    pauseOnHover: true,
    draggable: false,
    progress: undefined,
    theme: "light",
});

var name = null;
var email = null;
var address = null;
var mcgill_id = null;
var password = null;
var checkbox = null;

export default function Signup() {

    name = React.useRef();
    email = React.useRef();
    address = React.useRef();
    mcgill_id = React.useRef();
    password = React.useRef();
    checkbox = React.useRef();


    return (
        <div className='App-header'>
            <ParticlesComponent />
            <div className="title">
                <h1>Create an account</h1>
                <form className='form' onSubmit={post}>
                    <p>
                        <label>Name</label><br />
                        <input ref={name} type="text" name="name" required /><br />
                        <label></label><br />
                    </p>
                    <p>
                        <label>Email address</label><br />
                        <input ref={email} type="email" name="email" required /><br />
                        <label></label><br />
                    </p>
                    <p>
                        <label>Address</label><br />
                        <input ref={address} type="text" name="address" required /><br />
                        <label></label><br />
                    </p>
                    <p>
                        <label>McGill ID</label><br />
                        <input ref={mcgill_id} type='text' name="mcgill_id" required /><br />
                        <label></label><br />
                    </p>
                    <p>
                        <label>Password</label><br />
                        <input ref={password} type="password" name="password" required /><br />
                        <label></label><br />
                    </p>
                    <p>
                        <input ref={checkbox} type="checkbox" name="checkbox" id="checkbox" /> <span>I am a driver</span><br />
                        <label></label><br />
                    </p>
                    <p>
                        <ButtonCustom type="submit" style={{ height: "39px", width: "156px", fontSize: "20px" }} title="Submit" id="sub_btn"></ButtonCustom>
                    </p>
                    {/* <ToastContainer /> */}
                </form>
                <footer>
                    <button style={{ backgroundColor: 'transparent', border: 'none', cursor: 'pointer' }}><Link to="/login"><p>Already have an account?</p></Link></button>
                </footer>
            </div>
        </div>
    )



}
async function post(event) {
    event.preventDefault();
    let response = await fetch('http://localhost:5000/signup/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "name": name.current.value, "email": email.current.value, "address": address.current.value, "mcgill_id": mcgill_id.current.value, "password": password.current.value, "checkbox": checkbox.current.checked })
    })
    let result = await response.json();
    if (response.ok) {
        notifySuccess(result.message);
    } else {
        notifyError(result.message);
    }
}