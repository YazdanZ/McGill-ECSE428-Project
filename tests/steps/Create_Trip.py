import behave_webdriver
from behave import *
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



@given('The Driver is logged in to their drivers account with mihiranshul@gmail.com and name123')
def step_impl(context):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get('http://localhost:3000/login')
    context.behave_driver.find_element_by_id('email').send_keys('mihiranshul@gmail.com')
    context.behave_driver.find_element_by_id('password').send_keys('name123')
    context.behave_driver.find_element_by_id('checkbox').click()
    wait = WebDriverWait(context.behave_driver, 1)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button-container')))
    element.click()
    context.behave_driver.maximize_window()
    context.behave_driver.get('http://localhost:3000/createTrip')


@when('The Driver enters their total 20 covered in their trip')
def step_impl(context):
    context.behave_driver.maximize_window()
    context.behave_driver.get('http://localhost:3000/createTrip')
    context.behave_driver.find_element_by_id('distance_km').send_keys(20)
    wait = WebDriverWait(context.behave_driver, 1)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button-container')))
    element.click()


@then('The Driver gets a notification message stating "New Trip Created"')
def step_impl(context):
    WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
                                                  'Timed out waiting for PA creation ' +
                                                  'confirmation popup to appear.')
    alert = Alert(context.behave_driver)
    assert alert.text == "New Trip Created"
    context.behave_driver.quit()





@given('The Driver is logged in to their drivers account with mihir.kumar@yahoo.com and age456')
def step_impl(context):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get('http://localhost:3000/login')
    context.behave_driver.find_element_by_id('email').send_keys('mihir.kumar@yahoo.com')
    context.behave_driver.find_element_by_id('password').send_keys('age456')
    context.behave_driver.find_element_by_id('checkbox').click()
    wait = WebDriverWait(context.behave_driver, 1)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button-container')))
    element.click()
    context.behave_driver.maximize_window()
    context.behave_driver.get('http://localhost:3000/createTrip')


@when('The Driver enters their total 30 covered in their trip')
def step_impl(context):
    context.behave_driver.maximize_window()
    context.behave_driver.get('http://localhost:3000/createTrip')
    context.behave_driver.find_element_by_id('distance_km').send_keys(30)
    wait = WebDriverWait(context.behave_driver, 1)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button-container')))
    element.click()


@given('The Driver is logged in to their drivers account with kumarsingh56@hotmail.com and animal22')
def step_impl(context):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get('http://localhost:3000/login')
    context.behave_driver.find_element_by_id('email').send_keys('kumarsingh56@hotmail.com')
    context.behave_driver.find_element_by_id('password').send_keys('animal22')
    context.behave_driver.find_element_by_id('checkbox').click()
    wait = WebDriverWait(context.behave_driver, 1)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button-container')))
    element.click()
    context.behave_driver.maximize_window()
    context.behave_driver.get('http://localhost:3000/createTrip')


@when('The Driver enters their total 10 covered in their trip')
def step_impl(context):
    context.behave_driver.maximize_window()
    context.behave_driver.get('http://localhost:3000/createTrip')
    context.behave_driver.find_element_by_id('distance_km').send_keys(10)
    wait = WebDriverWait(context.behave_driver, 1)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button-container')))
    element.click()




@when('The Driver does not enter their total distance covered in their trip')
def step_impl(context):
    context.behave_driver.maximize_window()
    context.behave_driver.get('http://localhost:3000/createTrip')
    wait = WebDriverWait(context.behave_driver, 1)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button-container')))
    element.click()


@then('The Driver gets a notification message stating "Add Distance covered"')
def step_impl(context):
    WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
                                    'Timed out waiting for PA creation ' +
                                    'confirmation popup to appear.')
    alert = Alert(context.behave_driver)
    assert alert.text == "Add Distance covered"
    context.behave_driver.quit()
