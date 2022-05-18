#verify a new user has to login before being able to donate ie user is redirected to register screen on hitting donate

from pickle import TRUE
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
import time
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.maximize_window()  
driver.get("http://localhost:3000/")  
l = driver.find_element_by_name("donate-btn")
l.click()  
time.sleep(5)  