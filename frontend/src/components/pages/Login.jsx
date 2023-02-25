import React from 'react'
import { Link } from 'react-router-dom'
import ParticlesComponent from '../Particles'
import ButtonCustom from '../button/Button'
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import '../../App.css'
import { notifyError, notifySuccess } from './Signup';


var email = null;
var password = null;
var checkbox = null;
export default function Login() {

    email = React.useRef();
    password = React.useRef();
    checkbox = React.useRef();

    return (
        <div className='App-header'>
            <ParticlesComponent />
            <div className="title">
                <h1>Login to McPool</h1>
                <form className='form' onSubmit={post}>
                    <p>
                        <label>Email address</label><br />
                        <input ref={email} type="email" name="email" id="email" required /><br />
                        <label></label><br />
                    </p>
                    <p>
                        <label>Password</label><br />
                        <input ref={password} type="password" name="password" id="password" required /><br />
                        <label></label><br />
                    </p>
                    <p>
                        <input ref={checkbox} type="checkbox" name="checkbox" id="checkbox" /> <span>I am a driver</span><br />
                        <label></label><br />
                    </p>
                    <p>
                        <Link to='/user-info'>
                            <ButtonCustom name="submitter" type="submit" style={{ height: "39px", width: "156px", fontSize: "20px" }} title="Submit" id="sub_btn"></ButtonCustom>
                        </Link>
                    </p>
                    <ToastContainer />
                </form>
                <footer>
                    <button style={{ backgroundColor: 'transparent', border: 'none', cursor: 'pointer' }}><Link to="/"><p>Don't have an account?</p></Link></button>
                </footer>
            </div>
        </div>
    )

}



async function post(event) {
    event.preventDefault();
    let response = await fetch('http://localhost:5000/login/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "email": email.current.value, "password": password.current.value, "checkbox": checkbox.current.checked })
    })
    let result = await response.json();
    if (response.ok) {
        notifySuccess(result.message);
        window.location.href = '/user-info';

    } else {
        notifyError(result.message);
    }
}

