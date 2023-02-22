from flask import Flask, jsonify, make_response
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mcpool.db"
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


@app.route("/createUser/", methods=["POST"])
def createUser():
    data = request.get_json()

    user = User.query.filter_by(
        email=data['email']
    ).first()

    if user:
        # email already exists
        return jsonify({"message": "Email already exists"}), 401

    user = User.query.filter_by(
        mcgill_id=data['mcgill_id']
    ).first()

    if user:
        # mcgill_id already exists
        return jsonify({"message": "McGill ID already exists"}), 401

    user = User(
        name=data['name'],
        email=data['email'],
        address=data['address'],
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


@app.route("/getTrip", methods=['GET'])
def getTrip():
    user_email = request.args.get('userEmail')
    trip = Trip.query.filter(Trip.passengers.any(email=user_email)).first()
    data = {'message': 'User successfully created', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 201)

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



# getting everything in plain text! :(
@app.route("/login/", methods=["POST"])
def login():
    data = request.get_json()

    # make sure checkbox is "true" or "false" as strings
    user = User.query.filter_by(
        email=data["email"], password=data["password"], isDriver=data["checkbox"]
    ).first()

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
        #         name='Anandamoyi',
        #         email='anandamoyisaha17@gmail.com',
        #         mcgill_id=260924135,
        #         password='password',
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
        driver_name = driver.name
        driver_vehicle = trip.vehicle
        pickup_location = trip.pick_up_address
        dropoff_location = trip.drop_off_address
        fuel_consumption = trip.vehicle.fuel_consumption
        available_seats = trip.vehicle.seats 
        trip_dict = {
            'trip_id' : trip.trip_id,
            'distance_km' : trip.distance_km,
            'passenger_id' : trip.passenger_id,
             'passenger' : trip.passenger,
             'vehicle_id' : trip.vehicle_id,
              'driver_name': driver_name,
            'drop_off_address' : dropoff_location,
            'pick_up_address' : pickup_location,
            'fuel_consumption': fuel_consumption,
            'available_seats': available_seats

        }
        trip_list.append(trip_dict)
    return jsonify(trip_list), 200

@app.route("/assignPassenger/", methods=["POST"])
def assignPassenger():
    data = request.get_json()
    # user = User.query.filter_by(
    #     email=data['email']
    # ).first()
    db.session.query(Trip).filter(
        Trip.trip_id == data['trip_id']
    ).update(
        {
            Trip.passenger_id: data['email']
        }
    )
    
    try:
      
        db.session.commit()
        return jsonify({"message": "Passenger added successfully!"}), 200
    except:
        return jsonify({"message": "Unable to add passenger."})


if __name__ == "__main__":
     app.run(debug=True)
