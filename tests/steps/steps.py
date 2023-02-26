from behave import given, when, then
from selenium.webdriver.common.by import By
import time
import requests
import json


@given("I am on the sign-up page")
def step_impl(context):
    context.browser.get('http://localhost:3000/')
    time.sleep(2)


@when("I fill in my name, email, mcgill id, password, and driver status")
def step_impl(context):
    name_field = context.browser.find_element(By.NAME, 'name')
    name_field.send_keys('John Doe')
    email_field = context.browser.find_element(By.NAME, 'email')
    email_field.send_keys('himel.saha@ml.mcgill.ca')
    id_field = context.browser.find_element(By.NAME, 'mcgill_id')
    id_field.send_keys('2601356')
    password_field = context.browser.find_element(By.NAME, 'password')
    password_field.send_keys('password123')
    checkbox = context.browser.find_element(By.NAME, 'checkbox')
    checkbox.click()


@when("I click the 'Submit' button")
def step_impl(context):
    sign_up_button = context.browser.find_element(
        By.CLASS_NAME, 'button-container')
    sign_up_button.click()

@then("I should see a success message")
def step_impl(context):
    time.sleep(1)
    response = context.browser.find_element(By.CLASS_NAME, 'Toastify__toast')
    assert response.text == 'User successfully created'


@given("an account exists in the system with email 'johndoe@yahoo.com'")
def step_impl(context):
    payload = {
        "name": "John Doe",
        "email": "johndoe@yahoo.com",
        "mcgill_id": "260123",
        "password": "password123",
        "isDriver": "True"
    }

    json_payload = json.dumps(payload)

    headers = {
        "Content-Type": "application/json"
    }

    requests.post('http://localhost:5000/signup/', headers=headers, data=json_payload)

@when("I attempt to create an account with email 'johndoe@yahoo.com'")
def step_impl(context):
    name_field = context.browser.find_element(By.NAME, 'name')
    name_field.send_keys('John Doe')
    email_field = context.browser.find_element(By.NAME, 'email')
    email_field.send_keys('johndoe@yahoo.com')
    id_field = context.browser.find_element(By.NAME, 'mcgill_id')
    id_field.send_keys('26013156')
    password_field = context.browser.find_element(By.NAME, 'password')
    password_field.send_keys('password123')
    checkbox = context.browser.find_element(By.NAME, 'checkbox')
    checkbox.click()

@then("I should see an error message indicating email already exists in the system")
def step_impl(context):
    time.sleep(1)
    response = context.browser.find_element(By.CLASS_NAME, 'Toastify__toast')
    assert response.text == 'Email already exists'


@given("an account exists in the system with mcgill id '24356'")
def step_impl(context):
    payload = {
        "name": "Jane Doe",
        "email": "janedoe@yahoo.com",
        "mcgill_id": "24356",
        "password": "password123",
        "isDriver": "True"
    }

    json_payload = json.dumps(payload)

    headers = {
        "Content-Type": "application/json"
    }

    requests.post('http://localhost:5000/signup/', headers=headers, data=json_payload)

@when("I attempt to create an account with mcgill id '24356'")
def step_impl(context):
    name_field = context.browser.find_element(By.NAME, 'name')
    name_field.send_keys('Jane Doe')
    email_field = context.browser.find_element(By.NAME, 'email')
    email_field.send_keys('janedoe2@yahoo.com')
    id_field = context.browser.find_element(By.NAME, 'mcgill_id')
    id_field.send_keys('24356')
    password_field = context.browser.find_element(By.NAME, 'password')
    password_field.send_keys('password123')
    checkbox = context.browser.find_element(By.NAME, 'checkbox')
    checkbox.click()


@then("I should see an error message indicating mcgill id already exists in the system")
def step_impl(context):
    time.sleep(1)
    response = context.browser.find_element(By.CLASS_NAME, 'Toastify__toast')
    assert response.text == 'McGill ID already exists'



@when("I attempt to create an account with an invalid email address")
def step_impl(context):
    name_field = context.browser.find_element(By.NAME, 'name')
    name_field.send_keys('Jane Doe')
    email_field = context.browser.find_element(By.NAME, 'email')
    email_field.send_keys('janeyahoo')
    id_field = context.browser.find_element(By.NAME, 'mcgill_id')
    id_field.send_keys('24356')
    password_field = context.browser.find_element(By.NAME, 'password')
    password_field.send_keys('password123')
    checkbox = context.browser.find_element(By.NAME, 'checkbox')
    checkbox.click()

@then("I should see an error message indicating that the email address is invalid")
def step_impl(context):
    time.sleep(1)
    email_field = context.browser.find_element(By.NAME, 'email')
    validation_message = email_field.get_attribute("validationMessage")
    assert ('Please enter an email address' in validation_message)
