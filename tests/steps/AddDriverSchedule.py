from behave import *
import behave_webdriver
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import requests
import json

use_step_matcher("re")

@given('I am on the add-driver-schedule page')
def step_impl(context):
    # use this in firefox
    # context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # context.driver.get('http://localhost:3000/add-driver-schedule')
    # Use this in chrome
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get('http://localhost:3000/add-driver-schedule')

@when('I fill in the start date, start time, and trip id')
def step_impl(context):
    # use this in firefox
    # context.driver.find_element_by_id('start_date').send_keys('30/03/2023')
    # context.driver.find_element_by_id('start_time').send_keys('10:00')
    # context.driver.find_element_by_id('trip_id').send_keys(1)
    #use this in chrome
    context.behave_driver.find_element_by_id('start_date').send_keys('30/03/2023')
    context.behave_driver.find_element_by_id('start_time').send_keys('10:00')
    context.behave_driver.find_element_by_id('trip_id').send_keys(1)

@when('I click the Submit button')
def step_impl(context):
    # use this in firefox
    # wait = WebDriverWait(context.driver, 10)
    # element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    # element.click()
    # use this in chrome
    wait = WebDriverWait(context.behave_driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    element.click()

@then('I should see a success message')
def step_impl(context):
    # use this in firefox
    # WebDriverWait(context.driver, 3).until(EC.alert_is_present(),
    #                                               'Timed out waiting for PA creation ' +
    #                                               'confirmation popup to appear.')
    # alert = Alert(context.driver)
    # assert alert.text == "Schedule added successfully!"
    # context.driver.quit()
    # use this in chrome
    WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
                                                  'Timed out waiting for PA creation ' +
                                                  'confirmation popup to appear.')
    alert = Alert(context.behave_driver)
    assert alert.text == "Schedule added successfully!"
    context.behave_driver.quit()



@when('I fill in a non-existing trip id')
def step_impl(context):
    # use this in firefox
    # context.driver.find_element_by_id('start_date').send_keys('30/03/2023')
    # context.driver.find_element_by_id('start_time').send_keys('10:00')
    # context.driver.find_element_by_id('trip_id').send_keys(5)
    # use this in chrome
    context.behave_driver.find_element_by_id('start_date').send_keys('30/03/2023')
    context.behave_driver.find_element_by_id('start_time').send_keys('10:00')
    context.behave_driver.find_element_by_id('trip_id').send_keys(5)



@then('I should see an error message')
def step_impl(context):
    # use this in firefox
    # WebDriverWait(context.driver, 3).until(EC.alert_is_present(),
    #                                               'Timed out waiting for PA creation ' +
    #                                               'confirmation popup to appear.')
    # alert = Alert(context.driver)
    # assert alert.text == "Unable to add schedule."
    # context.driver.quit()
    # use this in chrome
    WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
                                                  'Timed out waiting for PA creation ' +
                                                  'confirmation popup to appear.')
    alert = Alert(context.behave_driver)
    assert alert.text == "Unable to add schedule."
    context.behave_driver.quit()