from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import behave_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

@given('I am on the Signup Page')
def step_impl(context):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get('http://localhost:3000')

@given(u'I am an existing user with email samiad2789@gmail.com and password mamama')
def step_impl(context):
    name_field = context.behave_driver.find_element(By.NAME, 'name')
    name_field.send_keys('Sami')
    email_field = context.behave_driver.find_element(By.NAME, 'email')
    email_field.send_keys('samiad2789@gmail.com')
    id_field = context.behave_driver.find_element(By.NAME, 'mcgill_id')
    id_field.send_keys('2601356')
    password_field = context.behave_driver.find_element(By.NAME, 'password')
    password_field.send_keys('mamama')
    wait = WebDriverWait(context.behave_driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    # Interact with the element
    element.click()
    time.sleep(5)

@given(u'I am logged in with email samiad2789@gmail.com and password mamama')
def step_impl(context):
    context.behave_driver.get('http://localhost:3000/login')
    context.behave_driver.find_element_by_id('email').send_keys('samiad2789@gmail.com')
    context.behave_driver.find_element_by_id('password').send_keys('mamama')
    wait = WebDriverWait(context.behave_driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    # Interact with the element
    element.click()
    time.sleep(5)

@given(u'I am an existing user with email samiad2766@gmail.com and password mamama')
def step_impl(context):
    context.behave_driver.get('http://localhost:3000')
    name_field = context.behave_driver.find_element(By.NAME, 'name')
    name_field.send_keys('Sami')
    email_field = context.behave_driver.find_element(By.NAME, 'email')
    email_field.send_keys('samiad2766@gmail.com')
    id_field = context.behave_driver.find_element(By.NAME, 'mcgill_id')
    id_field.send_keys('2601357')
    password_field = context.behave_driver.find_element(By.NAME, 'password')
    password_field.send_keys('mamama')
    wait = WebDriverWait(context.behave_driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    # Interact with the element
    element.click()
    time.sleep(5)

@given(u'I am logged in with email samiad2766@gmail.com and password mamama')
def step_impl(context):
    context.behave_driver.get('http://localhost:3000/login')
    context.behave_driver.find_element_by_id('email').send_keys('samiad2766@gmail.com')
    context.behave_driver.find_element_by_id('password').send_keys('mamama')
    wait = WebDriverWait(context.behave_driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    # Interact with the element
    element.click()
    time.sleep(5)

@given('I have no trip that I created')
def step_impl(context):
    time.sleep(2)

@given('I have one trip that I created')
def step_impl(context):
    context.behave_driver.get('http://localhost:3000/createTrip')

    wait5 = WebDriverWait(context.behave_driver, 3)
    select_element = wait5.until(EC.presence_of_element_located((By.ID, 'pickup')))
    select_element.click
    wait = WebDriverWait(context.behave_driver, 1)
    element2 = wait.until(EC.presence_of_element_located((By.ID, 'create_new_pickup')))
    element2.click()
    wait2 = WebDriverWait(context.behave_driver, 1)
    element3 = wait2.until(EC.presence_of_element_located((By.ID, 'pick_up_address_line_1')))
    element3.send_keys('1 Toad Road')
    context.behave_driver.find_element_by_id('pick_up_city').send_keys('Montreal')
    context.behave_driver.find_element_by_id('pick_up_postal_code').send_keys('H2W2J8')

    wait5 = WebDriverWait(context.behave_driver, 3)
    select_element = wait5.until(EC.presence_of_element_located((By.ID, 'dropoff')))
    select_element.click
    wait = WebDriverWait(context.behave_driver, 1)
    element2 = wait.until(EC.presence_of_element_located((By.ID, 'create_new_dropoff')))
    element2.click()
    wait2 = WebDriverWait(context.behave_driver, 1)
    element3 = wait2.until(EC.presence_of_element_located((By.ID, 'drop_off_address_line_1')))
    element3.send_keys('2 Toad Road')
    context.behave_driver.find_element_by_id('drop_off_city').send_keys('Montreal')
    context.behave_driver.find_element_by_id('drop_off_postal_code').send_keys('H2W2J8')
    context.behave_driver.find_element_by_id('distance_km').send_keys(25)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    # Interact with the element
    element.click()
    time.sleep(1)
    WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
                                                  'Timed out waiting for PA creation ' +
                                                  'confirmation popup to appear.')
    alert = context.behave_driver.switch_to.alert
    alert_text = alert.text
    alert.accept()

@when('I select to go to the passenger bill page')
def step_impl(context):
    context.behave_driver.get('http://localhost:3000/passenger-bill')

@then('I should be able to see the information corresponding to my trip in the passenger bill page')
def step_impl(context):
    time.sleep(3)
    div_element = context.behave_driver.find_element_by_xpath("//div")
    expected_text = [
        'Trip ID: 1',
        'Pickup location: 1 Toad Road, Montreal, H2W2J8',
        'Dropoff location: 2 Toad Road, Montreal, H2W2J8',
        'Total cost (CAD): 31.25',
        'Trip length (km): 25',
    ]
    child_elements = div_element.find_elements_by_xpath(".//*")
    actual_text = [element.text for element in child_elements]
    assert all(text in actual_text for text in expected_text)
    context.behave_driver.quit()

@then('I should not be able to see any new bill')
def step_impl(context):
    time.sleep(3)
    div_element = context.behave_driver.find_element_by_xpath("//div")
    expected_text = [
        'Trip ID: 2',
    ]
    child_elements = div_element.find_elements_by_xpath(".//*")
    actual_text = [element.text for element in child_elements]
    assert all(text not in actual_text for text in expected_text)
    context.behave_driver.quit()
