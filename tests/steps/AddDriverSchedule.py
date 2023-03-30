from behave import *
import behave_webdriver
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
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
    context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    context.driver.get('http://localhost:3000/add-driver-schedule')

@when('I fill in the start date, start time, and trip id')
def step_impl(context):
    context.driver.find_element_by_id('start_date').send_keys('30/03/2023')
    context.driver.find_element_by_id('start_time').send_keys('10:00')
    context.driver.find_element_by_id('trip_id').send_keys(1)

@when('I click the Submit button')
def step_impl(context):
    #wait = WebDriverWait(context.driver, 50)
    # context.driver.implicitly_wait(15)
    # #element = context.driver.find_element(By.XPATH, '//*[@id="sub_btn"]')
    # # element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='sub_btn']")))
    # # # Interact with the element
    # # element.click()
    # context.driver.find_element_by_id("bt").click()
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    element.click()

@then('I should see a success message')
def step_impl(context):
    WebDriverWait(context.driver, 3).until(EC.alert_is_present(),
                                                  'Timed out waiting for PA creation ' +
                                                  'confirmation popup to appear.')
    alert = Alert(context.driver)
    assert alert.text == "Schedule added successfully!"
    context.driver.quit()