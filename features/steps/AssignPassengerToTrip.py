from behave import *
import behave_webdriver
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import requests
import json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from backend.app import User

use_step_matcher("re")

@given('I am on the available trips page')
def step_impl(context):
    context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    context.driver.get('http://localhost:3000/display-trips')

@when('I enter an existing email address under the trip that I picked')
def step_impl(context):
    context.driver.find_element_by_id('email').send_keys('joe123@gmail.com')

@when('I click the Submit button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, "sub_btn")))
    # Interact with the element
    element.click()

@then('I should be assigned to the trip that I picked')
def step_impl(context):
    email = 'joe123@gmail.com'
    trip_id = 1
    user = User.query.filter_by(email=email).first()
    assert user is not None, f"No user found with email address {email}"
    assert any(trip.trip_id == trip_id for trip in user.passenger_trip), f"User with email {email} not assigned to trip {trip_id}"


