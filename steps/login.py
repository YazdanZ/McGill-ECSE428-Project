from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import behave_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the Login page')
def step_impl(context):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get('http://localhost:3000/login')

@when('I enter an existing email address and password')
def step_impl(context):
    context.behave_driver.find_element_by_id('email').send_keys('samiad2788@gmail.com')
    context.behave_driver.find_element_by_id('password').send_keys('mamama')

@when('I click the Submit button')
def step_impl(context):
    #button = context.browser.find_element_by_id("sub_btn")
    #button.click()
    #Wait up to 10 seconds for the element to be present
    wait = WebDriverWait(context.behave_driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    # Interact with the element
    element.click()

@when('I enter a non-existing email address and password')
def step_impl(context):
    context.behave_driver.find_element_by_id('email').send_keys('kasir@gmail.com')
    context.behave_driver.find_element_by_id('password').send_keys('mamama')

@then('I should be redirected to the UserInfo page')
def step_impl(context):
    assert context.behave_driver.current_url == 'http://localhost:3000/user-info'
    context.behave_driver.quit()

@then('An Error Message should be displayed')
def step_impl(context):
    context.behave_driver.quit()