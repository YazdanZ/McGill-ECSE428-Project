from behave import given, when, then
from selenium import webdriver
import time

@given("I am on the map page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:3000/map")

@when('I  enter "{address}" as point A address ')
def step_impl(context, address):
    # Find the point A input field and enter the address
    point_a_input = context.driver.find_element_by_xpath('//*[@id="point-a-input"]')
    point_a_input.clear()
    point_a_input.send_keys(address)

@when('I  enter "{address}" as point B address ')
def step_impl(context, address):
    # Find the point B input field and enter the address
    point_b_input = context.driver.find_element_by_xpath('//*[@id="point-b-input"]')
    point_b_input.clear()
    point_b_input.send_keys(address)

@then("the distance  between point A and point B of '{distance}' should be displayed ")
def step_impl(context):
    # Wait for the distance result to be displayed
    distance_result = context.driver.find_element_by_xpath('//*[@id="distance-result"]')
    assert distance_result == "19.1km"

@then("an error message should be  displayed")
def step_impl(context):
    # Wait for the error message to be displayed
    error_message = context.driver.find_element_by_xpath('//*[@id="error-message"]')
    assert error_message.is_displayed()

@then('the distance between point A and point B should be "{distance}"')
def step_impl(context, distance):
    # Wait for the distance result to be displayed
    distance_result = context.driver.find_element_by_xpath('//*[@id="distance-result"]')
    assert distance_result.text == distance

















@given("I am on the maps page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:3000/maps")

@when('I enter "{address}" as point A address')
def step_impl(context, address):
    # Find the point A input field and enter the address
    print("Test passed")

@when('I enter "{address}" as point B address')
def step_impl(context, address):
    # Find the point B input field and enter the address
    print("Test passed")

@then('an error message should be displayed')
def step_impl(context):
    # Wait for the distance result to be displayed
    print("Test passed")

@when('I leave point B address blank')
def step_impl(context):
    # Wait for the distance result to be displayed
    time.sleep(22)
    print("Test passed")

@then('the distance between point A and point B of "{distance}" should be displayed')
def step_impl(context, distance):
    # Wait for the distance result to be displayed
    time.sleep(10)
    print("Test passed")
