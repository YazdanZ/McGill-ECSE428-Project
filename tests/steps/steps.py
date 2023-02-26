from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("I am on the sign-up page")
def step_impl(context):
    context.browser.get('http://localhost:3000/')
    time.sleep(2)


@when("I fill in my name, email, mcgill id, password, and driver status")
def step_impl(context):
    name_field = context.browser.find_element(By.NAME, 'name')
    name_field.send_keys('John Doe')
    email_field = context.browser.find_element(By.NAME, 'email')
    email_field.send_keys('himel.saha@mal.mcgill.ca')
    id_field = context.browser.find_element(By.NAME, 'mcgill_id')
    id_field.send_keys('26013456')
    password_field = context.browser.find_element(By.NAME, 'password')
    password_field.send_keys('password123')
    checkbox = context.browser.find_element(By.NAME, 'checkbox')
    checkbox.click()


@when("I click the 'Submit' button")
def step_impl(context):
    sign_up_button = context.browser.find_element(By.CLASS_NAME, 'button-container')
    sign_up_button.click()


@then("I should see a success message")
def step_impl(context):
    time.sleep(1)
    response = context.browser.find_element(By.CLASS_NAME, 'Toastify__toast')
    assert response.text == 'User successfully created'


@when("I provide an invalid email address")
def step_impl(context):
    name_field = context.browser.find_element_by_name('emainame')
    name_field.send_keys('John Doe')
    email_field = context.browser.find_element_by_name('email')
    email_field.send_keys('my email')
    id_field = context.browser.find_element_by_name('mcgill_id')
    id_field.send_keys('260123456')
    password_field = context.browser.find_element_by_name('password')
    password_field.send_keys('password123')
    checkbox = context.browser.find_element_by_name('checkbox')
    checkbox.click()






@then("I should see an error message indicating that the email address is invalid")
def step_impl(context):
    error_message = context.browser.find_element_by_css_selector(
        '.error-message')
    assert error_message.text == "An account with this email address already exists."
