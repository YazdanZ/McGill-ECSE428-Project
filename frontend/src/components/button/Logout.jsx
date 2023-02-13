import React from 'react'
import { Link } from 'react-router-dom'
import ParticlesComponent from '../Particles'
import Userfront from "@userfront/core";

import '../../App.css'

export default function Logout() {

    return (
        <p>
            <button id="logout_btn" type="submit">
                Log out
            </button>
        </p>
    )

}