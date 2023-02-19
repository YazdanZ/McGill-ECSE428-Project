from flask import Flask, jsonify, make_response
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mcpool.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(50))
    mcgill_id = db.Column(db.Integer)
    password = db.Column(db.String(50))
    isDriver = db.Column(db.String(50))


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
        name = data['name'], 
        email = data['email'],
        address = data['address'],
        mcgill_id = data['mcgill_id'],
        password = data['password'],
        isDriver = data['checkbox'])
    
    db.session.add(user)
    db.session.commit()
    data = {'message': 'User successfully created', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 201)


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
