from behave import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from webdriver_manager.chrome import ChromeDriverManager
import behave_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'the passenger with email "mark@mail.com" and password "password" signs into the application')
def step_impl(context):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get('http://localhost:3000/login')
    context.behave_driver.find_element_by_id('email').send_keys('mark@mail.com')
    context.behave_driver.find_element_by_id('password').send_keys('password')

@when(u'the passenger accesses the Trip Display page to view trip information')
def step_impl(context):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get('http://localhost:3000/login')
    wait = WebDriverWait(context.behave_driver, 5)


@then(u'the passenger should see the trip details')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the passenger should see the trip details')


@given(u'the passenger with email "jane@mail.com" and password "password" signs into the application')
def step_impl(context):
    context.behave_driver = behave_webdriver.Chrome(ChromeDriverManager().install())
    context.behave_driver.get('http://localhost:3000/login')
    context.behave_driver.find_element_by_id('email').send_keys('jane@gmail.com')
    context.behave_driver.find_element_by_id('password').send_keys('password')


@then(u'the passenger should not see any trip details')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the passenger should not see any trip details')