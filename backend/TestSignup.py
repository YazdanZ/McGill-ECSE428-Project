import pytest
import requests
import json
from flask import Flask, jsonify, make_response
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from app import User, app



class TestSignup:

    def test_successful_signup(self):
        print("hello")
        url = 'http://localhost:5000/signup/'
        payload = {
            'name': 'John Doe',
            'email': 'tx@email.com',
            'mcgill_id': '9cxxxxx',
            'password': 'password123',
            'checkbox': True
        }
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))
    

        if response.ok:
            with app.app_context():
                user = User.query.filter_by(email='tx@example.com').first()
                print(user)
                assert user.name == 'John Doe'
                assert user.mcgill_id == '9cxxxxx'
                assert user.password == 'password123'
                assert user.checkbox == 'True'
