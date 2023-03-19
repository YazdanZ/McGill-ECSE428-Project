import React from 'react'
import { Link } from 'react-router-dom'
import ParticlesComponent from '../Particles'
import ButtonCustom from '../button/Button'

export default function Home() {

    const handleClick = () => {
        window.location.href = "/";
    }

    return (
        <p>
            <Link to="/" onClick={handleClick}>
                <ButtonCustom title="Home" id="home_btn" type="submit"></ButtonCustom>
            </Link>
        </p>
    )
}