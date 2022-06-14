from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def lanchBrowser():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    
    driver.get("https://www.how-to-type.com/typing-practice/quote/")
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
    #screenshot.show()
    #im.show()
    print(element, location, size, x, y, width, height)

getScreenshot()

def image_to_text():

    image = 'element.png'
    text = tess.image_to_string(Image.open(image), lang='eng')
    print(text)

image_to_text()

def closeBrowser():
    time.sleep(1)
    driver.close()
    return driver

closeBrowser()


'''
def image_to_text():
    reader = easyocr.Reader(['en'], gpu = False)
    image_file_name='element.png'
    image = cv2.imread(image_file_name)

    image_text = (reader.readtext(image,detail=0)[0])
    print(image_text)
image_to_text()

only works in py 2
'''
