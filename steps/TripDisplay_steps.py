import time
from behave import *
from webdriver_manager.chrome import ChromeDriverManager
import behave_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the passenger with email "mark@mail.com" and password "password" signs into the application')
def step_impl(context):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get('http://localhost:3000/login')
    context.behave_driver.find_element_by_id('email').send_keys('mark@mail.com')
    context.behave_driver.find_element_by_id('password').send_keys('password')
    time.sleep(3)
    wait = WebDriverWait(context.behave_driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    element.click()
    time.sleep(3)

@when('the passenger accesses the Trip Display page to view trip information')
def step_impl(context):
    context.behave_driver.get('http://localhost:3000/display-trip')
    time.sleep(3)

@then('the passenger should see the trip details')
def step_impl(context):
    expected_trip_details = {
        'Driver': 'Driver: Andrew',
        'Vehicle': 'Vehicle: Toyota Corolla',
        'Pickup Location': 'Pickup Location: 59 Sherbooke St, Montreal, H56 3A7',
        'Dropoff Location': 'Dropoff Location: 49 Boul Chomedey, Laval, J5Z 5E1',
        'Distance': 'Distance: 50 kilometers',
        'Duration': 'Duration: 30 minutes',
        'Cost': 'Cost: 50$\nView Details'
    }
    
    actual_trip_details = {
        'Driver': context.behave_driver.find_element_by_id('driver').text,
        'Vehicle': context.behave_driver.find_element_by_id('vehicle').text,
        'Pickup Location': context.behave_driver.find_element_by_id('pickup-location').text,
        'Dropoff Location': context.behave_driver.find_element_by_id('dropoff-location').text,
        'Distance': context.behave_driver.find_element_by_id('distance').text,
        'Duration': context.behave_driver.find_element_by_id('duration').text,
        'Cost': context.behave_driver.find_element_by_id('cost').text
    }
    
    assert expected_trip_details == actual_trip_details

@given('the passenger with email "jane@mail.com" and password "password" signs into the application')
def step_impl(context):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get('http://localhost:3000/login')
    context.behave_driver.find_element_by_id('email').send_keys('jane@mail.com')
    context.behave_driver.find_element_by_id('password').send_keys('password')
    time.sleep(3)
    wait = WebDriverWait(context.behave_driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    #Interact with the element
    element.click()
    time.sleep(3)

@then(u'the passenger should not see any trip details')
def step_impl(context):
    expected_trip_details = {
        'Driver': 'Driver:',
        'Vehicle': 'Vehicle:',
        'Pickup Location': 'Pickup Location:',
        'Dropoff Location': 'Dropoff Location:',
        'Distance': 'Distance: kilometers',
        'Duration': 'Duration: minutes',
        'Cost': 'Cost: $\nView Details'
    }
    
    actual_trip_details = {
        'Driver': context.behave_driver.find_element_by_id('driver').text,
        'Vehicle': context.behave_driver.find_element_by_id('vehicle').text,
        'Pickup Location': context.behave_driver.find_element_by_id('pickup-location').text,
        'Dropoff Location': context.behave_driver.find_element_by_id('dropoff-location').text,
        'Distance': context.behave_driver.find_element_by_id('distance').text,
        'Duration': context.behave_driver.find_element_by_id('duration').text,
        'Cost': context.behave_driver.find_element_by_id('cost').text
    }
    
    print(actual_trip_details)
    
    assert expected_trip_details == actual_trip_details