from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#association table between User and Trip to store passengers on a given trip
passengers_per_trip = db.Table('association', db.Column('user_id', db.String(50), db.ForeignKey('user_table.email')), db.Column('trip_id', db.Integer, db.ForeignKey('trip_table.trip_id')))

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
    trip_id = db.Column(db.Integer, primary_key=True)
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
    driver = db.relationship("User", back_populates="driver_car")
    vehicle_trip = db.relationship("Trip", back_populates="vehicle")