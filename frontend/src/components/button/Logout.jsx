import React from 'react'
import { Link } from 'react-router-dom'
import ParticlesComponent from '../Particles'
import ButtonCustom from '../button/Button'

import '../../App.css'

export default function Logout() {

    return (

        <p>
            <Link to="/">
                <ButtonCustom style={{ height: "39px", width: "156px", fontSize: "20px", top: '0', right: '0', position: 'absolute' }} title="Log Out" id="logout_btn" type="submit"></ButtonCustom>
            </Link>
        </p >
    )

}