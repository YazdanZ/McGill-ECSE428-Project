import React from 'react'
import ParticlesComponent from '../Particles'
import '../../App.css'

export default function EditUserInfo() {

    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="title">
                <h1>Edit User Info</h1>
                <form className='form'>
                    <p>
                        <label>Name:</label><br/>
                        <input type="text" name="name" required/><br/>
                        <label></label><br/>
                    </p>
                    <br/>
                    <p id>
                        <label>Email address:</label><br/>
                        <input type="email" name="email" required/><br/>
                        <label></label><br/>
                    </p>
                    <br/>
                    <p>
                        <label>McGill ID:</label><br/>
                        <input type='text' name="id" required/><br/>
                        <label></label><br/>
                    </p>
                    <br/>
                    <p> 
                        <button id="sub_btn" type="submit">Submit Changes</button>
                    </p>
                </form>
            </div>
        </div>
    )

}