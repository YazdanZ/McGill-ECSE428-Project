from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import behave_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@given('I am on the Signup Page')
def step_impl(context):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get('http://localhost:3000')

@given('I am an existing user with email samiad2788@gmail.com and password mamama')
def step_impl(context):
    context.behave_driver.find_element_by_id('name').send_keys('Sami')
    context.behave_driver.find_element_by_id('email').send_keys('samiad2788@gmail.com')
    context.behave_driver.find_element_by_id('mcgill_id').send_keys('2666666')
    context.behave_driver.find_element_by_id('password').send_keys('mamama')
    wait = WebDriverWait(context.behave_driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    # Interact with the element
    element.click()

@when('I am logged in with email samiad2788@gmail.com and password mamama')
def step_impl(context):
    context.behave_driver.get('http://localhost:3000/login')
    context.behave_driver.find_element_by_id('email').send_keys('samiad2788@gmail.com')
    context.behave_driver.find_element_by_id('password').send_keys('mamama')
    wait = WebDriverWait(context.behave_driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    # Interact with the element
    element.click()

@when('I have two trips that I created')
def step_impl(context):
    context.behave_driver.get('http://localhost:3000/createTrip')
    select = Select(context.behave_driver.find_element_by_id('pickup'))
    select.select_by_visible_text('Create New')
    context.behave_driver.find_element_by_id('pick_up_address_line_1').send_keys('1 Toad Road')
    context.behave_driver.find_element_by_id('pick_up_city').send_keys('Montreal')
    context.behave_driver.find_element_by_id('pick_up_postal_code').send_keys('H2W2J8')
    select = Select(context.behave_driver.find_element_by_id('dropoff'))
    select.select_by_visible_text('Create New')
    context.behave_driver.find_element_by_id('drop_off_address_line_1').send_keys('2 Toad Road')
    context.behave_driver.find_element_by_id('drop_off_city').send_keys('Montreal')
    context.behave_driver.find_element_by_id('drop_off_postal_code').send_keys('H2W2J9')
    context.behave_driver.find_element_by_id('distance_km').send_keys('25')
    wait = WebDriverWait(context.behave_driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    # Interact with the element
    element.click()

@when('I select to go to the passenger bill page')
def step_impl(context):
    context.behave_driver.get('http://localhost:3000/passenger_bill')

@then('I should be able to see the bills for the two trips I created')
def step_impl(context):
    context.behave_driver.quit()