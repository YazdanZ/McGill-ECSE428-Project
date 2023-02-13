import React from 'react'
import ParticlesComponent from '../Particles'
//import '../../App.css'

export default function Create_Trip()  {

    return (
        <div className='App-header'>
            <ParticlesComponent/>
            <div className="title" style={{width: "500px", height:"200px", top:"70px", left:"100px"}}>
                <h1>Create Trip</h1>
                <form className='form'>
                    <p>
                        <label>Vehicle Name</label><br/>
                        <input type="text" name="vehicle_name" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>Vehicle Number</label><br/>
                        <input type="text" name="vehicle_number" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>Initial Location</label><br/>
                        <input type="text" name="initial" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>Final Location</label><br/>
                        <input type='text' name="final" required /><br/>
                        <label></label><br/>
                    </p>
                    <p>
                        <label>Maximum Number of Passengers</label><br/>
                        <input type="text" name="passengers" required /><br/>
                        <label></label><br/>
                    </p>

                    <p>
                        <button id="sub_btn" type="submit">Submit</button>
                    </p>
                </form>

            </div>
            <div class="box" style={{width:"700px", height:"500px", border: "1px solid black", right:"130px", position:"absolute", top:"100px"}}></div>
                        <br/><br/><br/><br/><br/>
                        <h1 style={{color: "white", tab:"10"}}> MAP </h1>
        </div>
    )





}
