import pytest
import requests
import json
from flask import Flask, jsonify, make_response
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from app import User, app


class testGetAvailableTrips:

    def test_get_avail_trips(self):
        url = 'http://localhost:5000/getAvailableTrips/'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.get(url,headers=headers)
  

        if response.ok:
            with app.app_context():
                data = response.json()
                #print(data[0]['driver_name'])
                assert data[0]['trip_id'] == 2
                assert data[0]['distance_km'] == 30
                assert data[0]['passenger_id'] == "mihiranshul@gmail.com"
                assert data[0]['vehicle_id'] == 5
                assert data[0]['driver_name'] == "Anandamoyi"
                assert data[0]['fuel_consumption'] == 10
                assert data[0]['available_seats'] == 5
                print(" Acceptance Test getAvailableTrips passed")


                

ts = testGetAvailableTrips()
ts.test_get_avail_trips()

if __name__ == "__main__":
     app.run(debug=True)