import React from 'react'
import ParticlesComponent from '../Particles'
import '../../App.css'

export default function UserInfo() {

    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="user_info_title">
                <h1>User Information</h1>
                <form id='user_info_form'>
                    <p id="info_form_contents">
                        <div id='info'>
                            <label>Name:</label>
                        </div>
                        <br/>
                        <div id='info'>
                            <label>Aidan Jackson</label>
                        </div>
                            <label></label><br/>
                        <br/>
                        <div id='info'>
                            <label>Email Address:</label><br/>
                        </div>
                        <br/>
                        <div>
                            <label>aidan.jackson@mail.mcgill.ca</label><br/>
                        </div>
                            <label></label><br/>
                        <div id='info'>
                            <label>McGill ID:</label><br/>
                        </div>
                        <br/>
                        <div id='info'>
                            <label>260924686</label><br/>
                        </div>
                            <label></label><br/>
                        <br/>
                        <div className='edit_button_holder'>
                            <button id="info_btn" type="submit">Edit</button>
                        </div>
                    </p>
                </form>
            </div>
        </div>
    )

}