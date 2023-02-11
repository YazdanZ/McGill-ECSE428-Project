import React from 'react'
import { Link } from 'react-router-dom'
import ParticlesComponent from '../Particles'

import '../../App.css'

export default function Signup() {

    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="title">
                <h2>Create an account</h2>
                <form className='form'>
                    <p>
                        <label>Name</label><br/>
                        <input type="text" name="name" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>Email address</label><br/>
                        <input type="email" name="email" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>McGill ID</label><br/>
                        <input type='text' name="id" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>Password</label><br/>
                        <input type="password" name="password" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <input type="checkbox" name="checkbox" id="checkbox" /> <span>I am a driver</span><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <button id="sub_btn" type="submit">Register</button>
                    </p>
                </form>
                <footer>
                    <p>Already have an account?</p>
                </footer>
            </div>
        </div>
    )

}
