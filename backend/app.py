from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mcpool.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user_table"
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), primary_key=True)
    # address = db.Column(db.String(50))
    mcgill_id = db.Column(db.Integer)
    password = db.Column(db.String(50))
    isDriver = db.Column(db.String(50))
    passenger_trip = db.relationship("Trip", back_populates="passenger")
    driver_car = db.relationship("Car", back_populates="driver")


class Trip(db.Model):
    __tablename__ = "trip_table"
    trip_id = db.Column(db.Integer, primary_key=True)
    distance_km = db.Column(db.Integer)
    passenger_id = db.Column(db.Integer, db.ForeignKey("user_table.email"))
    passenger = db.relationship("User", back_populates="passenger_trip")
    vehicle_id = db.Column(db.Integer, db.ForeignKey("car_table.car_id"))
    vehicle = db.relationship("Car", back_populates="vehicle_trip")
    drop_off_address = db.relationship("Address", back_populates="drop_off")
    pick_up_address = db.relationship("Address", back_populates="pick_up")


class Car(db.Model):
    __tablename__ = "car_table"
    car_id = db.Column(db.Integer, primary_key=True)
    fuel_consumption = db.Column(db.Integer)  # km per gallon or smth
    seats = db.Column(db.Integer)
    driver_id = db.Column(db.Integer, db.ForeignKey("user_table.email"))
    driver = db.relationship("User", back_populates="driver_car")
    vehicle_trip = db.relationship("Trip", back_populates="vehicle")


class Address(db.Model):
    db.__tablename__ = "address_table"
    city = db.Column(db.String(100))
    address_line_1 = db.Column(db.String(200))
    postal_code = db.Column(db.String(50))
    address_id = db.Column(db.Integer, primary_key=True)
    # drop_off_trip = db.Column(db.Integer, db.ForeignKey("trip_table.trip_id"))
    drop_off = db.relationship("Trip", back_populates="drop_off_address")
    trip = db.Column(db.Integer, db.ForeignKey("trip_table.trip_id"))
    pick_up = db.relationship("Trip", back_populates="pick_up_address")


with app.app_context():
    db.create_all()


@app.route("/createUser", methods=['POST'])
def createUser():
    data = request.get_json()

    user = User(
        name=data['name'],
        email=data['email'],
        mcgill_id=data['mcgill_id'],
        password=data['password'],
        isDriver=data['checkbox'])

    db.session.add(user)
    db.session.commit()
    return "200"


@app.route("/createTrip", methods=['POST'])
def createTrip():
    data = request.get_json()

    trip = Trip(
        trip_id=data["trip_id"],
        vehicle_id=data["vehicle_id"],
        passenger_id=data["passenger_id"],
        distance_km=data['distance_km'])

    db.session.add(trip)
    db.session.commit()
    return "200"


# include passenger id parameter
@app.route("/getTrip", methods=['GET'])
def getTrip():
    passenger_id = request.args.get('passengerId')
    trip = Trip.query.filter(Trip.passengers.any(id=passenger_id)).first()

    if trip:
        driver = User.query.filter_by(
            id=trip.driver_id).first()  # not sure if we should have driver and passenger classes
        driver_name = driver.name
        driver_vehicle = driver.vehicle
        pickup_location = trip.pickup_location
        dropoff_location = trip.dropoff_location
        distance = trip.distance_km
        tripId = trip.trip_id
        # duration = calculate_duration(trip.distance_km) #find a way to calculate duration
        # cost = calculate_cost(trip.distance_km, trip.fuel_consumption) #find a way to calculate cost

        return {
            'driver_name': driver_name,
            'driver_vehicle': driver_vehicle,
            'pickup_location': pickup_location,
            'dropoff_location': dropoff_location,
            'distance': distance,
            'tripId': tripId
            # 'duration': duration,
            # 'cost': cost
        }
    else:
        return 'You are currently not signed up for any trip'
