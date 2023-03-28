import behave_webdriver
from behave import *
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import requests
import json
import random

def before_all(context):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())

def after_all(context):
    # cleanup after tests run
    context.behave_driver.quit()

@given('The user has an account with mcgill_id {int} already in the database')
def step_impl(context, i) :
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    body = { "name": "a", "email": "e{i}@mail.ca", "mcgill_id": i, "password": "pass", "isDriver": True }
    requests.post('http://localhost:5000/signup/', data=json.dumps(body), headers=headers)
    context.user_id = i

@then('two dropdown menus are displayed')
def step_then(context) :
    try:
        wait = WebDriverWait(context.behave_driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "pickupDropdown")))
    except:
        assert False
    try:
        wait = WebDriverWait(context.behave_driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "dropoffDropdown")))
    except:
        assert False

@when("The create trip page is opened with the user's mcgill_id parameter passed as a URL parameter")
def step_when(context) :
    context.behave_driver.get("http://localhost:3000/createTrip?passenger_id=" + str(context.user_id))

@then("the possible values for the dropdowns include the addresses associated with the user's previously created trips")
def step_then(context) :
    wait = WebDriverWait(context.behave_driver, 10)
    dropoff_element = wait.until(EC.presence_of_element_located((By.ID, "dropoffDropdown")))
    wait = WebDriverWait(context.behave_driver, 10)
    pickup_element = wait.until(EC.presence_of_element_located((By.ID, "pickupDropdown")))
    
    assert len(pickup_element.options) == len(dropoff_element.options)
    assert len(dropoff_element.options) > 3 # at least 2 addresses
    

@given('The user has already created one or more trips')
def step_given(context) :
    addresses = requests.get('http://localhost:5000/getAddresses?passenger_id={context.user_id}')
    if (len(addresses.json()) < 2):
        pickup = requests.post('http://localhost:5000/createPickUp',
                    headers = {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                        },
                    data = json.stringify({"city":'city1', "address_line_1":'line1_1', "postal_code":'postal1'}))
        dropoff = requests.post('http://localhost:5000/createDropOff',
                    headers = {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                        },
                    data = json.stringify({"city":'city2', "address_line_1":'line1_2', "postal_code":'postal2'}))
        requests.post('http://localhost:5000/createTrip',
            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body = json.dumps({"vehicle_id":1, "passenger_id":context.user_id, "distance_km":1, "drop_off_address_id":dropoff.json()['address_id'], "pick_up_address_id":pickup.json()['address_id']}))

@then('The user gets a notification message stating a new trip was created')
def step_then(context) :
    WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
                                                  'Timed out waiting for PA creation ' +
                                                  'confirmation popup to appear.')
    alert = Alert(context.behave_driver)
    assert alert.text == "New Trip Created"
    
@when('The user presses the submit button')
def step_when(context) :
    wait = WebDriverWait(context.behave_driver, 10)
    submit_btn = wait.until(EC.presence_of_element_located((By.ID, "sub_btn")))
    submit_btn.click()
    
@when('the user enters a valid value into the total distance field')
def step_when(context):
    random_int = random.randint(1, 1000)
    wait = WebDriverWait(context.behave_driver, 10)
    context.behave_driver.find_element_by_id('distance_km').send_keys(str(random_int))
    
@when('the user selects two different previously created addresses for both dropoff and pickup')
def step_when(context):
    wait = WebDriverWait(context.behave_driver, 10)
    dropoff_element = Select(wait.until(EC.presence_of_element_located((By.ID, "dropoffDropdown"))))
    wait = WebDriverWait(context.behave_driver, 10)
    pickup_element = Select(wait.until(EC.presence_of_element_located((By.ID, "pickupDropdown"))))
    if random.uniform(0, 1) > 0.5:
        dropoff_element.select_by_index(2)
        pickup_element.select_by_index(3)
    else:
        dropoff_element.select_by_index(3)
        pickup_element.select_by_index(2)

@when('the user does not make a valid selection for at least one of pickup and dropoff addresses')
def step_when(context):
    wait = WebDriverWait(context.behave_driver, 10)
    if random.uniform(0, 1) > 0.5:
        element = Select(wait.until(EC.presence_of_element_located((By.ID, "dropoffDropdown"))))
    else:
        element = Select(wait.until(EC.presence_of_element_located((By.ID, "pickupDropdown"))))
    element.select_by_index(0)

@then('The user gets a notification message stating one of the locations was not selected')
def step_then(context, ) :
    WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
                                                  'Timed out waiting for PA creation ' +
                                                  'confirmation popup to appear.')
    alert = Alert(context.behave_driver)
    assert alert.text == "Select a dropoff location." or alert.text == "Select a pickup location."

@when('the user selects the same previously created address for both dropoff and pickup')
def step_when(context, ) :
    wait = WebDriverWait(context.behave_driver, 10)
    dropoff_element = Select(wait.until(EC.presence_of_element_located((By.ID, "dropoffDropdown"))))
    wait = WebDriverWait(context.behave_driver, 10)
    pickup_element = Select(wait.until(EC.presence_of_element_located((By.ID, "pickupDropdown"))))
    if random.uniform(0, 1) > 0.5:
        dropoff_element.select_by_index(3)
        pickup_element.select_by_index(3)
    else:
        dropoff_element.select_by_index(2)
        pickup_element.select_by_index(2)
@then('The user gets a notification message stating the pickup and dropoff addresses must be different')
def step_then(context, ) :
    WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
                                                  'Timed out waiting for PA creation ' +
                                                  'confirmation popup to appear.')
    alert = Alert(context.behave_driver)
    assert alert.text == "Pickup and dropoff address must be different."