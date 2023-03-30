from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

def before_all(context):
    context.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

def after_all(context):
    context.browser.quit()
