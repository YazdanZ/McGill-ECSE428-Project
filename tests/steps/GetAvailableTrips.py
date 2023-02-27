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

use_step_matcher("re")



@given('There are available trips created')
def step_impl(context):
    context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    #context.driver.get('http://localhost:3000/createTrip')
    # context.behave_driver.find_element_by_id('available_seats').send_keys("6")
    # context.behave_driver.find_element_by_id('fuel_consumption').send_keys("20")
    # context.behave_driver.find_element_by_id('distance_km').send_keys("30")
    # context.behave_driver.find_element_by_id('pickup_location').send_keys("1")
    # context.behave_driver.find_element_by_id('dropoff_location').send_keys("2")

@when('I fetch the available trips data')
def step_impl(context):
    response = requests.get('http://localhost:5000/getAvailableTrips')
    print(response.content)  # print the response content for debugging
    data = response.json()
    print(data)  # print the parsed JSON data for debugging
    context.trips_data = data

@then('I should get the first trip data')
def step_impl(context):
    expected_data = {
        "available_seats": 5,
        "distance_km": 50,
        "driver_name": "Andrew",
        "drop_off_address": "49 Boul Chomedey, Laval, J5Z 5E1",
        "fuel_consumption": 15,
        "pick_up_address": "59 Sherbooke St, Montreal, H56 3A7",
        "trip_id": 1,
        "vehicle_name": "Toyota Corolla"
    }
    data = context.trips_data
    print(data)  # print the trips data for debugging
    assert data[0] == expected_data

@when('I go to the available trips page')
def step_impl(context):
    print("Navigating to http://localhost:3000/display-trips...")
    context.driver.get('http://localhost:3000/display-trips')
    # seats_data = context.driver.find_element_by_xpath('//div[@class="centered"]/div[1]/label[2]')
    # distance_data = context.driver.find_element_by_xpath('//div[@class="centered"]/div[1]/label[3]')
    # driver_name_data = context.driver.find_element_by_xpath('//div[@class="centered"]/div[1]/label[4]')
    # drop_off_data = context.driver.find_element_by_xpath('//div[@class="centered"]/div[1]/label[5]')
    # fuel_data = context.driver.find_element_by_xpath('//div[@class="centered"]/div[1]/label[6]')
    # pick_up_data = context.driver.find_element_by_xpath('//div[@class="centered"]/div[1]/label[7]')
    # vehicle_data = context.driver.find_element_by_xpath('//div[@class="centered"]/div[1]/label[8]')
    seats_data = context.driver.find_element_by_xpath('//label[contains(text(),"Number of seats")]')
    distance_data = context.driver.find_element_by_xpath('//label[contains(text(),"Distance in km")]')
    driver_name_data = context.driver.find_element_by_xpath('//label[contains(text(),"Driver")]')
    drop_off_data = context.driver.find_element_by_xpath('//label[contains(text(),"Drop off address")]')
    fuel_data = context.driver.find_element_by_xpath('//label[contains(text(),"Fuel consumption")]')
    pick_up_data = context.driver.find_element_by_xpath('//label[contains(text(),"Pick up address")]')
    vehicle_data = context.driver.find_element_by_xpath('//label[contains(text(),"Vehicle type")]')
    available_seats = seats_data.text
    distance = distance_data.text
    driver_name = driver_name_data.text
    drop_off = drop_off_data.text
    fuel = fuel_data.text
    pick_up = pick_up_data.text
    vehicle = vehicle_data.text

    #print(available_seats)
    seats_available = int(available_seats.split(":")[-1].strip())
    context.distance = int(distance.split(":")[-1].strip())
    context.driver_name = driver_name.split(":")[-1].strip()
    context.drop_off = drop_off.split(":")[-1].strip()
    context.fuel = int(fuel.split(":")[-1].strip())
    context.pick_up = pick_up.split(":")[-1].strip()
    context.vehicle = vehicle.split(":")[-1].strip()
    context.seats = seats_available
    

@then('I should be able to see all of the available trips')
def step_impl(context):
    
    # seats_data = context.driver.find_element_by_xpath('//div[@class="centered"]/div[1]/label[2]')
    # available_seats = seats_data.text
    # seats_available = int(available_seats.split(":")[-1].strip())
     
     assert context.seats == 5
     assert context.distance == 50
     assert context.driver_name == "Andrew"
     assert context.drop_off == "49 Boul Chomedey, Laval, J5Z 5E1"
     assert context.fuel == 15
     assert context.pick_up == "59 Sherbooke St, Montreal, H56 3A7"
     assert context.vehicle == "Toyota Corolla"
    
     context.driver.quit()
