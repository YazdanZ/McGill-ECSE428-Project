import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import EditUserInfo from './components/pages/EditUserInfo'
import UserInfo from './components/pages/UserInfo'
import Signup from './components/pages/Signup'
import Logout from './components/button/Logout'
import Login from './components/pages/Login'
import Create_Trip from './components/pages/Create_Trip'
import TripDisplay from './components/pages/TripDisplay'
import DisplayTripCost from './components/pages/DisplayTripCost'
import AvailableDrivers from './components/pages/AvailableDrivers'

import './App.css'

export default function App() {
  return (
    <BrowserRouter>
      <div className='App'>
        <Routes>
          <Route path="/" element={<Signup />} />
          <Route path='/edit-user' element={<EditUserInfo />} />
          <Route path='/user-info' element={<UserInfo />} />
          <Route path='/logout' element={<Logout />} />
          <Route path='/login' element={<Login />} />
          <Route path='/createTrip' element={<Create_Trip />} />
          <Route path='/display-trip' element={<TripDisplay />} />
          <Route path='/trip-cost' element={<DisplayTripCost />} />
        </Routes>
        <Footer />
      </div>
    </BrowserRouter >
  )
}

const Footer = () => {
  return (
    <p className="text-center" style={FooterStyle}>Made by McGillians, for McGillians</p>
  )
}

const FooterStyle = {
  background: "#222",
  fontSize: ".8rem",
  color: "#fff",
  position: "absolute",
  bottom: 0,
  padding: "1rem",
  marginTop: "5rem",
  width: "100%",
  opacity: ".5"
}

