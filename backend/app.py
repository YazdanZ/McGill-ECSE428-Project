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
    address_id = db.Column(db.Integer, primary_key=True)
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

    if data['checkbox'] == True:
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

    trip = Trip(
        vehicle_id=data["vehicle_id"],
        distance_km=data['distance_km'],
        drop_off_address_id=data['drop_off_address_id'],
        pick_up_address_id=data['pick_up_address_id']

    )

    if trip.distance_km == "":
        return jsonify({"message": "Add Distance covered"}), 401

    else:
        db.session.add(trip)
        db.session.commit()
        return jsonify({"message": "New Trip Created"}), 200


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
        driver_email = trip.vehicle.driver.name
        driver_vehicle = trip.vehicle.vehicle_description
        pickup_location = trip.pick_up_address.address_line_1 + ', ' + trip.pick_up_address.city + ', ' + trip.pick_up_address.postal_code
        dropoff_location = trip.drop_off_address.address_line_1 + ', ' + trip.drop_off_address.city + ', ' + trip.drop_off_address.postal_code
        distance = trip.distance_km
        trip_id = trip.trip_id
        fuel_consumption = trip.vehicle.fuel_consumption
        num_seats = trip.vehicle.seats
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
        #user = User.query.filter_by(email="mihiranshul@gmail.com").first()
        driver_name = driver.name
        driver_vehicle = trip.vehicle
        pickup_location = pick_up_address.address_line_1 + ", " + pick_up_address.city + ", " + pick_up_address.postal_code
        dropoff_location = drop_off_address.address_line_1 + ", " + drop_off_address.city + ", " + drop_off_address.postal_code
        fuel_consumption = trip.vehicle.fuel_consumption
        available_seats = trip.vehicle.seats
        
        trip_dict = {
            'trip_id' : trip.trip_id,
            'distance_km' : trip.distance_km,
            #'passenger_id' : trip.passenger_id,
             #'passenger' : trip.passenger,
             'vehicle_name' : car.vehicle_description,
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

# adds a passenger to a trip, for the time being used it to test Trip Display
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
