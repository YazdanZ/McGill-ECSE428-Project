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
    cars = db.relationship("Car",back_populates="driver_relation")
    trips = db.relationship("Trip",back_populates="passengers_relation")

class Trip(db.Model):
    trip_id = db.Column(db.Integer, primary_key=True)
    distance_km = db.Column(db.Integer)
    passengers = db.Column(db.String(50), db.ForeignKey('user.email'), nullable=True)
    passengers_relation = db.relationship("User", back_populates="trips")
    vehicle = db.Column(db.Integer, db.ForeignKey('car.car_id'), nullable=False)
    vehicle_relation = db.relationship("Car", back_populates="trips")
    pickup_location = db.Column(db.String(100), db.ForeignKey('address.address_id'), nullable=False)
    dropoff_location = db.Column(db.String(100), db.ForeignKey('address.address_id'), nullable=False)
    pickup_address = db.relationship("Address", back_populates="pickup_trips", foreign_keys=[pickup_location])
    dropoff_address = db.relationship("Address", back_populates="dropoff_trips", foreign_keys=[dropoff_location])
    
class Car(db.Model):
    car_id = db.Column(db.Integer, primary_key=True)
    driver = db.Column(db.Integer, db.ForeignKey('user.email'), nullable=False)
    driver_relation = db.relationship("User", back_populates="cars")
    trips = db.relationship("Trip",back_populates="vehicle_relation")
    fuel_consumption = db.Column(db.Integer) #km per gallon or smth
    seats = db.Column(db.Integer)
    
class Address(db.Model):
    city = db.Column(db.String(100))
    address_line_1 = db.Column(db.String(200))
    pickup_trips = db.relationship("Trip", back_populates="pickup_address", uselist=False, foreign_keys="Trip.pickup_location")
    dropoff_trips = db.relationship("Trip", back_populates="dropoff_address", uselist=False, foreign_keys="Trip.dropoff_location")
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

@app.route("/getTrip", methods = ['GET'])
def getTrip():
    user_email = request.args.get('userEmail')
    trip = Trip.query.filter(Trip.passengers.any(email=user_email)).first()

    if trip:
        driver = User.query.filter_by(email=trip.vehicle.driver).first()
        driver_name = driver.name
        driver_vehicle = trip.vehicle.car_id
        pickup_location = trip.pickup_address.address_line_1 + ", " + trip.pickup_address.city
        dropoff_location = trip.dropoff_address.address_line_1 + ", " + trip.dropoff_address.city
        distance = trip.distance_km
        trip_id = trip.trip_id
        fuel_consumption = trip.vehicle.fuel_consumption
        available_seats = trip.vehicle.seats - len(trip.passengers)

        return {
            'driver_name': driver_name,
            'driver_vehicle': driver_vehicle,
            'pickup_location': pickup_location,
            'dropoff_location': dropoff_location,
            'distance': distance,
            'trip_id': trip_id,
            'fuel_consumption': fuel_consumption,
            'available_seats': available_seats
        }
    else:
        return 'You are currently not signed up for any trip'