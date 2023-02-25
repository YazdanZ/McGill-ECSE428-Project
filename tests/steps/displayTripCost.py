from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import behave_webdriver
from selenium.webdriver.common.by import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

@given("A trip with trip_id 12345 exists in the database")
def step_impl(context):
    r = requests.post("http://localhost:5000/createTrip", data={"trip_id":12345,"vehicle_id":12345,"passenger_id":'e@mail.com',"distance_km":10})

@when("The displayTripCost page is opened with trip_id 12345 parameter passed through the URL")
def step_impl(context):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get("http://localhost:3000/trip-cost?trip_id=12345")

@then("The trip_id, total cost in CAD, number of passengers, available seats, cost per passenger, trip length, estimated fuel consumption, and estimated C02 saved for the trip with ID 12345 is displayed")
def step_impl(context):
    try:
        wait = WebDriverWait(context.behave_driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "tripid")))
    finally:
        assert False
    try:
        wait = WebDriverWait(context.behave_driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "cost")))
    finally:
        assert False
    try:
        wait = WebDriverWait(context.behave_driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "passengers")))
    finally:
        assert False
    try:
        wait = WebDriverWait(context.behave_driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "seats")))
    finally:
        assert False
    try:
        wait = WebDriverWait(context.behave_driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "costpp")))
    finally:
        assert False
    try:
        wait = WebDriverWait(context.behave_driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "length")))
    finally:
        assert False
    try:
        wait = WebDriverWait(context.behave_driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "fuel")))
    finally:
        assert False
    try:
        wait = WebDriverWait(context.behave_driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "c02")))
    finally:
        assert False

@then("A link to return to the trip display page is displayed")
def step_impl(context):
    try:
        wait = WebDriverWait(context.behave_driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "return_link")))
    finally:
        assert False

@when("The link to return to the trip display page is selected")
def step_impl(context):
    wait = WebDriverWait(context.behave_driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "return_link")))
    element.click()

@then("The trip display page is displayed")
def step_impl(context):
    assert context.behave_driver.current_url == "http://localhost:3000/display-trip"
    context.behave_driver.quit()
