from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def lanchBrowser():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    
    driver.get("https://www.how-to-type.com/typing-practice/quote/")
    return driver
driver = lanchBrowser()

def getScreenshot():
    driver.save_screenshot('ss.png')
    


def closeBrowser():
    time.sleep(10)
    driver.close()
    return driver

closeBrowser()
