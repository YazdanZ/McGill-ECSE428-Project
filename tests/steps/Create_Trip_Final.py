# import behave_webdriver
# from behave import *
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager


# @given(u'The Driver is logged in to their drivers account with mihir.kumar@mail.mcgill.ca and anshul123')
# def step_impl(context):
#     context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
#     context.behave_driver.get('http://localhost:3000/login')
#     context.behave_driver.find_element_by_id('email').send_keys('mihir.kumar@mail.mcgill.ca')
#     context.behave_driver.find_element_by_id('password').send_keys('anshul123')
#     context.behave_driver.find_element_by_id('checkbox').click()
#     wait = WebDriverWait(context.behave_driver, 1)
#     element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button-container')))
#     element.click()
#     context.behave_driver.maximize_window()
#     #context.behave_driver.get('http://localhost:3000/createTrip')





# @when(u'The Driver enters their 5678 Stanley Street')
# def step_impl(context):
#     context.behave_driver.maximize_window()
#     context.behave_driver.get('http://localhost:3000/createTrip')
#     wait5 = WebDriverWait(context.behave_driver, 1)
#     select_element = wait5.until(EC.presence_of_element_located((By.ID, 'pickupDropdown')))
#     #select_element = context.behave_driver.find_element(By.ID, 'select_pickup')
#     select_element.click
#     wait = WebDriverWait(context.behave_driver, 1)
#     element2 = wait.until(EC.presence_of_element_located((By.ID, 'create_new_pickup')))
#     element2.click()
#     wait2 = WebDriverWait(context.behave_driver, 1)
#     element3 = wait2.until(EC.presence_of_element_located((By.ID, 'pick_up_address_line_1')))
#     element3.send_keys('5678 Stanley Street')




# @when(u'The Driver enters their Montreal')
# def step_impl(context):
#     context.behave_driver.find_element_by_id('pick_up_city').send_keys('Montreal')

# @when(u'The Driver enters their Laval')
# def step_impl(context):
#     context.behave_driver.find_element_by_id('drop_off_city').send_keys('Laval')



# @when(u'The Driver enters their H2FC7T')
# def step_impl(context):
#     context.behave_driver.find_element_by_id('pick_up_postal_code').send_keys('H2FC7T')


# @when(u'The Driver enters their 3440 Parc Avenue')
# def step_impl(context):
#     #context.behave_driver.maximize_window()
#     #context.behave_driver.get('http://localhost:3000/createTrip')
#     select_element = context.behave_driver.find_element(By.ID, 'dropoffDropdown')
#     select_element.click
#     wait = WebDriverWait(context.behave_driver, 1)
#     element2 = wait.until(EC.presence_of_element_located((By.ID, 'create_new_dropoff')))
#     element2.click()
#     wait2 = WebDriverWait(context.behave_driver, 1)
#     element3 = wait2.until(EC.presence_of_element_located((By.ID, 'drop_off_address_line_1')))
#     element3.send_keys('3440 Parc Avenue')


# @when(u'The Driver enters their H2XB3B')
# def step_impl(context):
#     context.behave_driver.find_element_by_id('drop_off_postal_code').send_keys('H2XB3B')


# @when(u'The Driver enters their total 30 covered in their trip')
# def step_impl(context):
#     ##context.behave_driver.maximize_window()
#    # context.behave_driver.get('http://localhost:3000/createTrip')
#     context.behave_driver.find_element_by_id('distance_km').send_keys(30)
#     wait = WebDriverWait(context.behave_driver, 1)
#     element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button-container')))
#     element.click()

# @then(u'The Driver gets a notification message stating "New Trip Created"')
# def step_impl(context):
#     WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
#                                                   'Timed out waiting for PA creation ' +
#                                                   'confirmation popup to appear.')
#     alert = Alert(context.behave_driver)
#     assert alert.text == "New Trip Created"
#     context.behave_driver.quit()

# @when('The Driver does not enter their total distance covered in their trip')
# def step_impl(context):
#     #context.behave_driver.maximize_window()
#     #context.behave_driver.get('http://localhost:3000/createTrip')
#     wait = WebDriverWait(context.behave_driver, 1)
#     element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button-container')))
#     element.click()

# @then('The Driver gets a notification message stating "Set a total distance."')
# def step_impl(context):
#     WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
#                                     'Timed out waiting for PA creation ' +
#                                     'confirmation popup to appear.')
#     alert = Alert(context.behave_driver)
#     assert alert.text == "Set a total distance."
#     context.behave_driver.quit()


# @when(u'The Driver does not enter their pick up address line 1')
# def step_impl(context):
#     context.behave_driver.maximize_window()
#     context.behave_driver.get('http://localhost:3000/createTrip')
#     wait5 = WebDriverWait(context.behave_driver, 1)
#     select_element = wait5.until(EC.presence_of_element_located((By.ID, 'pickupDropdown')))
#     # select_element = context.behave_driver.find_element(By.ID, 'select_pickup')
#     select_element.click
#     wait = WebDriverWait(context.behave_driver, 1)
#     element2 = wait.until(EC.presence_of_element_located((By.ID, 'create_new_pickup')))
#     element2.click()
#     wait2 = WebDriverWait(context.behave_driver, 1)
#     element3 = wait2.until(EC.presence_of_element_located((By.ID, 'pick_up_address_line_1')))
#     element3.send_keys('')

# @then(u'The Driver gets a notification message stating "Add Pick up Address Line"')
# def step_impl(context):
#     WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
#                                                   'Timed out waiting for PA creation ' +
#                                                   'confirmation popup to appear.')
#     alert = Alert(context.behave_driver)
#     assert alert.text == "Add Pick up Address Line"
#     context.behave_driver.quit()


# @then(u'The Driver gets a notification message stating "Add Pick up City"')
# def step_impl(context):
#     WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
#                                                   'Timed out waiting for PA creation ' +
#                                                   'confirmation popup to appear.')
#     alert = Alert(context.behave_driver)
#     assert alert.text == "Add Pick up City"
#     context.behave_driver.quit()

# @when(u'The Driver does not enter their pick up address city')
# def step_impl(context):
#     context.behave_driver.find_element_by_id('pick_up_city').send_keys('')


# @then(u'The Driver gets a notification message stating "Add Pick up Postal Code"')
# def step_impl(context):
#     WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
#                                                   'Timed out waiting for PA creation ' +
#                                                   'confirmation popup to appear.')
#     alert = Alert(context.behave_driver)
#     assert alert.text == "Add Pick up Postal Code"
#     context.behave_driver.quit()


# @when(u'The Driver does not enter their pick up address postal code')
# def step_impl(context):
#     context.behave_driver.find_element_by_id('pick_up_postal_code').send_keys('')

# @then(u'The Driver gets a notification message stating "Add Drop off Address Line"')
# def step_impl(context):
#     WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
#                                                   'Timed out waiting for PA creation ' +
#                                                   'confirmation popup to appear.')
#     alert = Alert(context.behave_driver)
#     assert alert.text == "Add Drop off Address Line"
#     context.behave_driver.quit()

# @when(u'The Driver does not enter their drop off address line 1')
# def step_impl(context):
#     #context.behave_driver.maximize_window()
#     #context.behave_driver.get('http://localhost:3000/createTrip')
#     select_element = context.behave_driver.find_element(By.ID, 'dropoffDropdown')
#     select_element.click
#     wait = WebDriverWait(context.behave_driver, 1)
#     element2 = wait.until(EC.presence_of_element_located((By.ID, 'create_new_dropoff')))
#     element2.click()
#     wait2 = WebDriverWait(context.behave_driver, 1)
#     element3 = wait2.until(EC.presence_of_element_located((By.ID, 'drop_off_address_line_1')))
#     element3.send_keys('')


# @then(u'The Driver gets a notification message stating "Add Drop off City"')
# def step_impl(context):
#     WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
#                                                   'Timed out waiting for PA creation ' +
#                                                   'confirmation popup to appear.')
#     alert = Alert(context.behave_driver)
#     assert alert.text == "Add Drop off City"
#     context.behave_driver.quit()

# @when(u'The Driver does not enter their drop off address city')
# def step_impl(context):
#     context.behave_driver.find_element_by_id('drop_off_city').send_keys('')


# @then(u'The Driver gets a notification message stating "Add Drop off Postal Code"')
# def step_impl(context):
#     WebDriverWait(context.behave_driver, 3).until(EC.alert_is_present(),
#                                                   'Timed out waiting for PA creation ' +
#                                                   'confirmation popup to appear.')
#     alert = Alert(context.behave_driver)
#     assert alert.text == "Add Drop off Postal Code"
#     context.behave_driver.quit()

# @when(u'The Driver does not enter their drop off address postal code')
# def step_impl(context):
#     context.behave_driver.find_element_by_id('drop_off_postal_code').send_keys('')