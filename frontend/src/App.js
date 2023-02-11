import React from 'react'
import Signup from './components/pages/TripDisplay'

import './App.css'

export default function App() {
    return (
      <div className='App'>
        <Signup/>
        <Footer/>
      </div>
    )
}

const Footer = () => {
  return (
      <p className="text-center" style={ FooterStyle }>Made by McGillians, for McGillians</p>
  )
}

const FooterStyle = {
  background: "#222",
  fontSize: ".8rem",
  color: "#fff",
  position: "absolute",
  bottom: 0,
  padding: "1rem",
  margin: 0,
  width: "100%",
  opacity: ".5"
}

