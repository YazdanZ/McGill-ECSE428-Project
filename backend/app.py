from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mcpool.db'
db = SQLAlchemy(app)

class User(db.Model):
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), primary_key=True)
    address = db.Column(db.String(50))
    mcgill_id = db.Column(db.Integer)
    password = db.Column(db.String(50))
    isDriver = db.Column(db.String(50))
    cars = db.relationship("Car",back_populates="driver")
    trips = db.relationship("Trip",back_populates="passengers")

class Trip(db.Model):
    trip_id = db.Column(db.Integer, primary_key=True)
    distance_km = db.Column(db.Integer)
    passengers = db.Column(db.String(50), db.ForeignKey('user.email'), nullable=True)
    vehicle = db.Column(db.Integer, db.ForeignKey('car.car_id'), nullable=False)
    pickup_location = db.Column(db.String(100), db.ForeignKey('address.address_id'), nullable=False)
    dropoff_location = db.Column(db.String(100), db.ForeignKey('address.address_id'), nullable=False)
    pickup_address = db.relationship("Address", back_populates="pickup_trips")
    dropoff_address = db.relationship("Address", back_populates="dropoff_trips")
    
class Car(db.Model):
    car_id = db.Column(db.Integer, primary_key=True)
    driver = db.Column(db.Integer, db.ForeignKey('user.email'), nullable=False)
    trips = db.relationship("Trip",back_populates="vehicle")
    fuel_consumption = db.Column(db.Integer) #km per gallon or smth
    seats = db.Column(db.Integer)
    
class Address(db.Model):
    city = db.Column(db.String(100))
    address_line_1 = db.Column(db.String(200))
    pickup_trips = db.relationship("Trip",back_populates="pickup_location", uselist=False)
    dropoff_trips = db.relationship("Trip",back_populates="dropoff_location", uselist=False)
    postal_code = db.Column(db.String(50))
    address_id = db.Column(db.Integer, primary_key=True)

with app.app_context():
    db.create_all()

@app.route("/createUser", methods = ['POST'])
def createUser():
    data = request.get_json()

    user = User(
        name = data['name'], 
        email = data['email'],
        mcgill_id = data['mcgill_id'],
        password = data['password'],
        isDriver = data['checkbox'])
    
    db.session.add(user)
    db.session.commit()
    return "200"

@app.route("/createTrip", methods = ['POST'])
def createTrip():
    data = request.get_json()

    trip = Trip(
        trip_id = data['trip_id'], 
        driver_id = data['driver_id'],
        passengers = data['passengers'],
        available_seats = data['available_seats'],
        fuel_consumption = data['fuel_consumption'],
        distance_km = data['distance_km'],
        pickup_location = data['pickup_location'],
        dropoff_location = data['dropoff_location'])
    
    db.session.add(trip)
    db.session.commit()
    return "200"

#include passenger id parameter
@app.route("/getTrip", methods = ['GET'])
def getTrip():
    passenger_id = request.args.get('passengerId')
    trip = Trip.query.filter(Trip.passengers.any(id=passenger_id)).first()

    if trip:
        driver = User.query.filter_by(id=trip.driver_id).first() #not sure if we should have driver and passenger classes
        driver_name = driver.name
        driver_vehicle = driver.vehicle
        pickup_location = trip.pickup_location
        dropoff_location = trip.dropoff_location
        distance = trip.distance_km
        tripId = trip.trip_id
        #duration = calculate_duration(trip.distance_km) #find a way to calculate duration
        #cost = calculate_cost(trip.distance_km, trip.fuel_consumption) #find a way to calculate cost

        return {
            'driver_name': driver_name,
            'driver_vehicle': driver_vehicle,
            'pickup_location': pickup_location,
            'dropoff_location': dropoff_location,
            'distance': distance,
            'tripId': tripId
            #'duration': duration,
            #'cost': cost
        }
    else:
        return 'You are currently not signed up for any trip'