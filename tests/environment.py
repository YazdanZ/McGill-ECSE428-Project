from selenium import webdriver

def before_all(context):
    #context.browser = webdriver.Chrome()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # to run Chrome in headless mode
    context.browser = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver.exe', options=chrome_options)

def after_all(context):
    context.browser.quit()
