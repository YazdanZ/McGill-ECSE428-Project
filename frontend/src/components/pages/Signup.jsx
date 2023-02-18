import React from 'react'
import ParticlesComponent from '../Particles'
import '../../styles.scss'
import ButtonCustom from '../button/Button'
import { Link } from 'react-router-dom'

export default function Signup() {

    return (
        <div className='App-header'>
            <ParticlesComponent />
            <div className="title">
                <h1>Create an account</h1>
                <form className='form'>
                    <p>
                        <label>Name</label><br />
                        <input type="text" name="name" required /><br />
                        <label></label><br />
                    </p>
                    <p>
                        <label>Email address</label><br />
                        <input type="email" name="email" required /><br />
                        <label></label><br />
                    </p>
                    <p>
                        <label>McGill ID</label><br />
                        <input type='text' name="mcgill_id" required /><br />
                        <label></label><br />
                    </p>
                    <p>
                        <label>Password</label><br />
                        <input type="password" name="password" required /><br />
                        <label></label><br />
                    </p>
                    <p>
                        <input type="checkbox" name="checkbox" id="checkbox" /> <span>I am a driver</span><br />
                        <label></label><br />
                    </p>
                    <p>
                        <ButtonCustom onClick={post} style={{ height: "39px", width: "156px", fontSize: "20px" }} title="Submit" id="sub_btn" type="button"></ButtonCustom>
                    </p>
                </form>
                <footer>
                    <button style={{ backgroundColor: 'transparent', border: 'none', cursor: 'pointer' }}><Link to="/login"><p>Already have an account?</p></Link></button>
                </footer>
            </div>
        </div>
    )

}
function post() {

    let form = document.querySelector("form");

 

        let formdata = new FormData(this);
        let name = formdata.get("name");
        let email = formdata.get("email");
        let mcgill_id = formdata.get("mcgill_id");
        let password = formdata.get("password");
        let checkbox = formdata.get("checkbox");
        if (checkbox == null) {
            checkbox = "False"
        } else {
            checkbox = "True"
        }

        fetch('http://localhost:5000/createUser', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ "name": name, "email": email, "mcgill_id": mcgill_id, "password": password, "checkbox": checkbox })
        })
            .then(response => alert("New user created"))

}

