import React from 'react'
import ParticlesComponent from '../Particles'
import '../../App.css'
import Logout from '../button/Logout'
import { Link } from 'react-router-dom'
import ButtonCustom from '../button/Button'

export default function UserInfo() {

    return (
        <div className='App-header'>
            <ParticlesComponent />
            <div className="user_info_title">
                <Logout />
                <h1>User Information</h1>
                <form id='user_info_form'>
                    <p id="info_form_contents">
                        <div id='info'>
                            <label>Name:</label>
                        </div>
                        <br />
                        <div id='info'>
                            <label>Aidan Jackson</label>
                        </div>
                        <label></label><br />
                        <br />
                        <div id='info'>
                            <label>Email Address:</label><br />
                        </div>
                        <br />
                        <div>
                            <label>aidan.jackson@mail.mcgill.ca</label><br />
                        </div>
                        <label></label><br />
                        <div id='info'>
                            <label>McGill ID:</label><br />
                        </div>
                        <br />
                        <div id='info'>
                            <label>260924686</label><br />
                        </div>
                        <label></label><br />
                        <br />
                        <div className='edit_button_holder'>
                            <ButtonCustom onclick="window.location.href='http://localhost:3000/edit-user'" type=" submit" style={{ height: "39px", width: "156px", fontSize: "20px" }} title="Submit" id="sub_btn"></ButtonCustom>
                        </div>
                        {/* <div>
                            <ButtonCustom type="submit" style={{ height: "39px", width: "156px", fontSize: "20px" }} title="Delete" id="del_btn"></ButtonCustom>
                        </div> */}
                    </p>
                </form>
            </div>
        </div>
    )

}