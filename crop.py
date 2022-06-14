from selenium import webdriver
from PIL import Image

driver = webdriver.Chrome()
driver.get("https://www.how-to-type.com/typing-practice/quote/")
element = driver.find_element_by_id("lesson-container")
location = element.location
size = element.size
driver.save_screenshot('sss.png')

driver.quit()