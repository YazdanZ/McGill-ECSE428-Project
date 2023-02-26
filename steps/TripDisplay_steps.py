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
    #Interact with the element
    element.click()
    time.sleep(3)

@when('the passenger accesses the Trip Display page to view trip information')
def step_impl(context):
    context.behave_driver.get('http://localhost:3000/display-trip')
    time.sleep(3)

@then(u'the passenger should see the trip details')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the passenger should see the trip details')

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
    raise NotImplementedError(u'STEP: Then the passenger should not see any trip details')