import React from 'react'
import ParticlesComponent from '../Particles'
import '../../App.css'
import '../button/Logout'
import Logout from '../button/Logout'
import { Link } from 'react-router-dom'
import { ToastContainer, toast } from 'react-toastify';
import ButtonCustom from '../button/Button'


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
var mcgill_id = null;
var password = null;
var original_email = null;

export default function EditUserInfo() {

    name = React.useRef();
    mcgill_id = React.useRef();
    password = React.useRef();
    original_email = React.useRef();

    return (
        <div className='App-header'>
            <ParticlesComponent />
            <div className="title">
                <Logout />
                <h1>Edit User Info</h1>
                <form className='form' onSubmit={post}>
                    <p>
                        <label>Name:</label><br />
                        <input ref={name} type="text" name="name" required /><br />
                        <label></label><br />
                    </p>
                    <br />
                    <p>
                        <label>original email:</label><br />
                        <input ref={name} type="text" name="original_email" required /><br />
                        <label></label><br />
                    </p>
                    <br />
                    <p>
                        <label>McGill ID:</label><br />
                        <input ref={mcgill_id} type='text' name="mcgill_id" required /><br />
                        <label></label><br />
                    </p>
                    <br />
                    <p>
                        <label>Password:</label><br />
                        <input ref={password} type='text' name="password" required /><br />
                        <label></label><br />
                    </p>
                    <br />
                    <p>
                        <ButtonCustom type="submit" style={{ height: "39px", width: "156px", fontSize: "20px" }} title="Submit" id="sub_btn"></ButtonCustom>
                    </p>
                    <ToastContainer/>
                </form>
            </div>
        </div>
    )

}

async function post(event) {
    event.preventDefault();
    let response = await fetch('http://localhost:5000/edit-user/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "name": name.current.value, "mcgill_id": mcgill_id.current.value, "password": password.current.value, "original_email": original_email.current.value})
    })
    let result = await response.json();
    if (response.ok) {
        notifySuccess(result.message);
        window.location.href = 'https://localhost:3000/user-info/';
    } else {
        notifyError(result.message);
    }
}