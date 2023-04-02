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
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

@given('I am not on the home page')
def step_impl(context):
    context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    context.driver.get('http://localhost:3000/user-info')

@when('I use the home button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 50)
    element = wait.until(EC.visibility_of_element_located((By.ID, "home_btn")))
    # Interact with the element
    element.click()
@then('I should be sent back to the home page')
def step_impl(context):
    time.sleep(2)
    assert context.behave_driver.current_url == 'http://localhost:3000'
    context.behave_driver.quit()
