from flask import Flask, jsonify, make_response
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mcpool.db"
db = SQLAlchemy(app)

# association table between User and Trip to store passengers on a given trip
passengers_per_trip = db.Table('association', db.Column('user_id', db.String(50), db.ForeignKey('user_table.email')),
                               db.Column('trip_id', db.Integer, db.ForeignKey('trip_table.trip_id')))


class User(db.Model):
    __tablename__ = "user_table"
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), primary_key=True)
    mcgill_id = db.Column(db.Integer)
    password = db.Column(db.String(50))
    isDriver = db.Column(db.String(50))
    passenger_trip = db.relationship("Trip", secondary=passengers_per_trip, back_populates="passengers")
    driver_car = db.relationship("Car", back_populates="driver")


class Trip(db.Model):
    __tablename__ = "trip_table"
    trip_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    distance_km = db.Column(db.Integer)
    passengers = db.relationship("User", secondary=passengers_per_trip, back_populates="passenger_trip")
    vehicle_id = db.Column(db.Integer, db.ForeignKey("car_table.car_id"))
    vehicle = db.relationship("Car", back_populates="vehicle_trip")
    drop_off_address_id = db.Column(db.Integer, db.ForeignKey("address_table.address_id"))
    drop_off_address = db.relationship("Address", back_populates="drop_off_trips", foreign_keys=[drop_off_address_id])
    pick_up_address_id = db.Column(db.Integer, db.ForeignKey("address_table.address_id"))
    pick_up_address = db.relationship("Address", back_populates="pick_up_trips", foreign_keys=[pick_up_address_id])


class Address(db.Model):
    __tablename__ = "address_table"
    address_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(100))
    address_line_1 = db.Column(db.String(200))
    postal_code = db.Column(db.String(50))
    drop_off_trips = db.relationship("Trip", back_populates="drop_off_address", foreign_keys=[Trip.drop_off_address_id])
    pick_up_trips = db.relationship("Trip", back_populates="pick_up_address", foreign_keys=[Trip.pick_up_address_id])


class Car(db.Model):
    __tablename__ = "car_table"
    car_id = db.Column(db.Integer, primary_key=True)
    vehicle_description = db.Column(db.String(100))
    fuel_consumption = db.Column(db.Integer)  # km per gallon or smth
    seats = db.Column(db.Integer)
    driver_id = db.Column(db.Integer, db.ForeignKey("user_table.email"))
    driver = db.relationship("User", back_populates="driver_car", lazy="joined")
    vehicle_trip = db.relationship("Trip", back_populates="vehicle", lazy="joined")


with app.app_context():
    db.create_all()

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    user = bool(User.query.filter_by(
        email=data['email']
    ).first())

    if user:
        # email already exists
        return jsonify({"message": "Email already exists"}), 401

    user = bool(User.query.filter_by(
        mcgill_id=data['mcgill_id']
    ).first())

    if user:
        # mcgill_id already exists
        return jsonify({"message": "McGill ID already exists"}), 401

    if data['isDriver'] == True:
        isDriver = "True"
    else:
        isDriver = "False"
    user = User(
        name=data['name'],
        email=data['email'],
        mcgill_id=data['mcgill_id'],
        password=data['password'],
        isDriver=isDriver)

    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User successfully created"}), 200


@app.route("/createTrip", methods=['POST'])
def createTrip():
    data = request.get_json()

    user = User.query.filter_by(mcgill_id=data["passenger_id"]).first()

    dropoff = Address.query.filter_by(address_id=data["drop_off_address_id"]).first()
    pickup = Address.query.filter_by(address_id=data["pick_up_address_id"]).first()

    trip = Trip(
        vehicle_id=data["vehicle_id"],
        distance_km=data['distance_km'],
        drop_off_address_id=data['drop_off_address_id'],
        pick_up_address_id=data['pick_up_address_id']
    )

    if trip.distance_km == "":
        return jsonify({"message": "Add Distance covered"}), 401
    else:
        if user: trip.passengers.append(user)
        db.session.add(trip)
        dropoff.drop_off_trips.append(trip)
        pickup.pick_up_trips.append(trip)
        db.session.commit()
        return jsonify({"message": "New Trip Created"}), 200
    

@app.route("/createPickUp", methods=['POST'])
def createPickUp():
    data = request.get_json()

    location = Address.query.filter_by(
        city=data['city'],
        address_line_1=data['address_line_1'],
        postal_code=data['postal_code']
    ).first()

    if location:
        return jsonify(address_id=location.address_id)

    pick_up = Address(
        city=data["city"],
        address_line_1=data['address_line_1'],
        postal_code=data['postal_code']

    )

    if pick_up.city == "":
        return jsonify({"message": "Add Pick up City"}), 401

    if pick_up.address_line_1 == "":
        return jsonify({"message": "Add Pick up Address Line"}), 401

    if pick_up.postal_code == "":
        return jsonify({"message": "Add Pick up Postal Code"}), 401

    else:
        db.session.add(pick_up)
        db.session.commit()
        # return jsonify({"message": "New Trip Created"}), 200

        return jsonify(address_id=pick_up.address_id)


@app.route("/createDropOff", methods=['POST'])
def createDropOff():
    data = request.get_json()

    location2 = Address.query.filter_by(
        city=data['city'],
        address_line_1=data['address_line_1'],
        postal_code=data['postal_code']
    ).first()

    if location2:
        return jsonify(address_id=location2.address_id)

    drop_off = Address(
        city=data["city"],
        address_line_1=data['address_line_1'],
        postal_code=data['postal_code']

    )

    if drop_off.city == "":
        return jsonify({"message": "Add Drop off City"}), 401

    if drop_off.address_line_1 == "":
        return jsonify({"message": "Add Drop off Address Line"}), 401

    if drop_off.postal_code == "":
        return jsonify({"message": "Add Drop off Postal Code"}), 401

    else:
        db.session.add(drop_off)
        db.session.commit()
        return jsonify(address_id=drop_off.address_id)

@app.route("/getAddresses", methods=['GET'])
def getAddresses():
    if 'passenger_id' in request.args:
        passenger_id = request.args.get('passenger_id')
        trips = Trip.query.filter(Trip.passengers.any(mcgill_id=passenger_id)).all()
        addresses = []
        for trip in trips:
            if trip.pick_up_address not in addresses: addresses.append(trip.pick_up_address)
            if trip.drop_off_address not in addresses: addresses.append(trip.drop_off_address)
    else:
        return jsonify({'error': 'Invalid request. Must include "passenger_id" argument.'})
    addresses = [ {"id":address.address_id, "address": str(address.address_line_1) + ", " + str(address.postal_code) + ", " + str(address.city)} for address in addresses]
    return jsonify(addresses)

@app.route("/getTrip", methods=['GET'])
def getTrip():
    if 'passenger_id' in request.args:
        passenger_id = request.args.get('passenger_id')
        trip = Trip.query.filter(Trip.passengers.any(email=passenger_id)).first()
    elif 'trip_id' in request.args:
        trip_id = request.args.get('trip_id')
        trip = Trip.query.get(trip_id)
    else:
        return jsonify({'error': 'Invalid request. Must include at least one of "userEmail" or "trip_id" arguments.'})

    if trip:
        try:
            driver_email = trip.vehicle.driver.name
            driver_vehicle = trip.vehicle.vehicle_description
            fuel_consumption = trip.vehicle.fuel_consumption
            num_seats = trip.vehicle.seats
        except AttributeError:
            driver_email = "null"
            driver_vehicle = "null"
            fuel_consumption = 999
            num_seats = 5
        pickup_location = trip.pick_up_address.address_line_1 + ', ' + trip.pick_up_address.city + ', ' + trip.pick_up_address.postal_code
        dropoff_location = trip.drop_off_address.address_line_1 + ', ' + trip.drop_off_address.city + ', ' + trip.drop_off_address.postal_code
        distance = trip.distance_km
        trip_id = trip.trip_id
        num_passengers = len(trip.passengers)

        return {
            'driver_name': driver_email,
            'driver_vehicle': driver_vehicle,
            'pickup_location': pickup_location,
            'dropoff_location': dropoff_location,
            'distance': distance,
            'trip_id': trip_id,
            'fuel_consumption': fuel_consumption,
            'num_seats': num_seats,
            'num_passengers': num_passengers,
            'cost': 50,  # cost will be calculated in a later sprint
            'duration': 30  # duration will be calculated in a later sprint
        }

    else:
        return jsonify({'error': 'Could not find trip for arguments {}'.format(request.args.items())})


@app.route('/trips/driver/<string:driver_email>', methods=['GET'])
def get_trips_by_driver(driver_email):
    driver = User.query.filter_by(email=driver_email, isDriver='True').first()
    if driver:
        trips = []
        for car in driver.driver_car:
            car_trips = Trip.query.filter_by(vehicle_id=car.car_id).all()
            trips.extend(car_trips)
        trips_json = []
        for trip in trips:
            trip_dict = {
                "trip_id": trip.trip_id,
                "pick_up_address": trip.pick_up_address.address_line_1 + ", " + trip.pick_up_address.city + ", " + trip.pick_up_address.postal_code,
                "drop_off_address": trip.drop_off_address.address_line_1 + ", " + trip.drop_off_address.city + ", " + trip.drop_off_address.postal_code,
                "available_seats": trip.vehicle.seats - len(trip.passengers),
                "passenger_names": [passenger.name for passenger in trip.passengers]
            }
            trips_json.append(trip_dict)
        return make_response(jsonify(trips_json), 200)
    else:
        return make_response(jsonify({"error": "Driver not found."}), 404)
    
@app.route('/deleteTrips/<int:trip_id>', methods=['DELETE'])
def delete_trip(trip_id):
    trip = Trip.query.get(trip_id)
    if trip:
        db.session.delete(trip)
        db.session.commit()
        return make_response(jsonify({"message": f"Trip with ID {trip_id} has been deleted."}), 200)
    else:
        return make_response(jsonify({"error": f"Trip with ID {trip_id} not found."}), 404)

# getting everything in plain text! :(
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    # make sure checkbox is "true" or "false" as strings
    user = User.query.filter_by(
        email=data["email"], password=data["password"], isDriver=str(data["checkbox"])).first()

    if user:
        # User exists and password is correct
        return jsonify({"message": "Login successful!"}), 200
    else:
        # User does not exist or password is incorrect
        return jsonify({"message": "Invalid email or password"}), 401


@app.route("/getAvailableDrivers/", methods=["GET"])
def getAvailableDrivers():
    users = User.query.filter_by(isDriver="True").all()

    user_list = []
    for user in users:
        user_dict = {
            'name': user.name,
            'email': user.email,
            'address': user.address,
            'mcgill_id': user.mcgill_id,
            'isDriver': user.isDriver,
        }
        user_list.append(user_dict)
    return jsonify(user_list), 200


@app.route("/getAvailableTrips/", methods=["GET"])
def getAvailableTrips():
    trips = Trip.query.all()

    trip_list = []
    for trip in trips:
        # user = User(
        #         name='Joe',
        #         email='joe123@gmail.com',
        #         mcgill_id=260901234,
        #         password='password12798698',
        #         isDriver='True'
        #    )
        # db.session.add(user)
        # db.session.commit()

        # car = Car(
        #     car_id=trip.vehicle_id,
        #     fuel_consumption=10,
        #     seats=5,
        #     driver=user
        # )
        # db.session.add(car)
        # db.session.commit()

        car = Car.query.filter_by(car_id=trip.vehicle_id).first()
        driver = User.query.filter_by(email=car.driver_id).first()
        pick_up_address = Address.query.filter_by(address_id=trip.pick_up_address_id).first()
        drop_off_address = Address.query.filter_by(address_id=trip.drop_off_address_id).first()
        # user = User.query.filter_by(email="mihiranshul@gmail.com").first()
        driver_name = driver.name
        driver_vehicle = trip.vehicle
        pickup_location = pick_up_address.address_line_1 + ", " + pick_up_address.city + ", " + pick_up_address.postal_code
        dropoff_location = drop_off_address.address_line_1 + ", " + drop_off_address.city + ", " + drop_off_address.postal_code
        fuel_consumption = trip.vehicle.fuel_consumption
        available_seats = trip.vehicle.seats

        trip_dict = {
            'trip_id': trip.trip_id,
            'distance_km': trip.distance_km,
            # 'passenger_id' : trip.passenger_id,
            # 'passenger' : trip.passenger,
            'vehicle_name': car.vehicle_description,
            'driver_name': driver_name,
            'drop_off_address': dropoff_location,
            'pick_up_address': pickup_location,
            'fuel_consumption': fuel_consumption,
            'available_seats': available_seats

        }
        trip_list.append(trip_dict)
    return jsonify(trip_list), 200


@app.route("/assignPassenger/", methods=["POST"])
def assignPassenger():
    pass


## adds a passenger to a trip, for the time being used it to test Trip Display
@app.route("/addPassengerToTrip", methods=['POST'])
def addPassengerToTrip():
    data = request.get_json()
    # user = User(
    #             name='Anandamoyi',
    #             email='anandamoyi.saha@mail.mcgill.ca',
    #             mcgill_id=260812345,
    #             password='password12',
    #             isDriver='False'
    #        )
    # db.session.add(user)
    # db.session.commit()
    user1 = User.query.filter_by(
        email=data['email']
    ).first()
    trip = Trip.query.filter_by(
        trip_id=data['trip_id']
    ).first()
    trip.passengers.append(user1)

    try:

        db.session.commit()
        return jsonify({"message": "Passenger added successfully!"}), 200
    except:
        return jsonify({"message": "Unable to add passenger."})


if __name__ == "__main__":
    app.run(debug=True)
