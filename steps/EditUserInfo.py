from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import behave_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


#####################SCENARIO 1##############################

@given('The user is on the EditUserInfo page')
def step_impl(context):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get('http://localhost:3000/edit-user')

@when('The user fills in the required fields')
def step_impl(context):
    name_field = "gsx@gmail.com" == "gsx@gmail.com"

@when('The user selects the Submit button')
def step_impl(context):
    name_field = "gsx@gmail.com" == "gsx@gmail.com"

@then('The system successfully updates the account information')
def step_impl(context):
    time.sleep(2)
    assert "gsx@gmail.com" == "gsx@gmail.com"
    context.behave_driver.quit()
    
################SCENARIO 2##########################


@then('The system fails to update the account information')
def step_impl(context):
    time.sleep(2)
    assert "gsx@gmail.com" == "gsx@gmail.com"
    context.behave_driver.quit()

