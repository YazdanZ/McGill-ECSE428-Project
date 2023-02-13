import React from 'react'
import { Link } from 'react-router-dom'
import ParticlesComponent from '../Particles'

import '../../App.css'

export default function Login() {

    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="title">
                <h1>Login to McPool</h1>
                <form className='form'>
                    <p>
                        <label>Email address</label><br/>
                        <input type="email" name="email" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>Password</label><br/>
                        <input type="password" name="password" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <button id="sub_btn" type="submit">Login</button>
                    </p>
                </form>
                <footer>
                    <p>Don't have an account?</p>
                </footer>
            </div>
        </div>
    )

}
