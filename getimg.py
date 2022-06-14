from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from PIL import Image

def lanchBrowser():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    
    driver.get("https://www.how-to-type.com/typing-practice/quote/")
    time.sleep(4)
    return driver

driver = lanchBrowser()

def getScreenshot():
    '''
    navigates to website and takes screenshot
    crops image off of quote class
    shows final product
    '''
    # navigation and image capture
    element = driver.find_element_by_id("content")
    location = element.location
    size = element.size
    driver.save_screenshot('ss.png')

    # crop image
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']
    im = Image.open('ss.png')
    im = im.crop((x+650, y+800, width+1070, height+100))
    im.save('element.png')   

    # shows results
    screenshot = Image.open('ss.png')
    screenshot.show()
    im.show()
    print(element, location, size, x, y, width, height)

getScreenshot()


def closeBrowser():
    time.sleep(3)
    driver.close()
    return driver

closeBrowser()
