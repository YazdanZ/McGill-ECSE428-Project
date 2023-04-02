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
                <ButtonCustom style={{ height: "39px", width: "156px", fontSize: "20px", left: '100', position: 'relative' }} title="Home" id="home_btn" type="submit"></ButtonCustom>
            </Link>
        </p>
    )
}