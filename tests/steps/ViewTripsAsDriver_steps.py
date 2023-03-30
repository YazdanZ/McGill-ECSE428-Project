import time
from behave import *
from webdriver_manager.chrome import ChromeDriverManager
import behave_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am logged in as a driver with email "{email}" and password "{password}"')
def step_impl(context, email, password):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get('http://localhost:3000/login')
    context.behave_driver.find_element_by_id('email').send_keys(email)
    context.behave_driver.find_element_by_id('password').send_keys(password)
    checkbox_element = context.behave_driver.find_element_by_id("checkbox")
    checkbox_element.click()
    time.sleep(3)
    wait = WebDriverWait(context.behave_driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-container")))
    element.click()
    time.sleep(3)

@when('I go to the "ViewTripsAsDriver" page')
def step_impl(context):
    context.behave_driver.get('http://localhost:3000/view-trips-as-driver')
    time.sleep(3)

@then('I should see a list of my created trips')
def step_impl(context):
    table_rows = context.behave_driver.find_elements_by_xpath("//table/tbody/tr")
    assert len(table_rows) > 0

@then('the trip should be deleted from the list')
def step_impl(context):
    rows = context.driver.find_elements_by_xpath("//table/tbody/tr")
    num_rows_after_delete = len(rows)
    assert num_rows_after_delete == context.num_rows_before_delete - 1, "Delete did not work"

@then('I should see no trips listed on the page')
def step_impl(context):
    table_rows = context.behave_driver.find_elements_by_xpath("//table/tbody/tr")
    assert len(table_rows) == 0

@when('I click the "Cancel" button for the first trip')
def step_impl(context):
    context.num_rows_before_delete = len(context.driver.find_elements_by_xpath("//table/tbody/tr"))
    cancel_button = context.driver.find_element_by_xpath("//table/tbody/tr[1]//button[contains(text(), 'Cancel')]")
    cancel_button.click()
  
#===========================================================================================
#Method to suppress the warning given in the cucumber file, the first given clause works but
#for some reason still triggers a warning
@given('I am logged in as a driver with email {string} and password {string}')
def step_given(context, string, string2) :
    pass

#Method to suppress the warning given in the cucumber file, the first given clause works but
#for some reason still triggers a warning
@when('I click the {string} button for trip {string}')
def step_when(context, string, string2) :
    pass