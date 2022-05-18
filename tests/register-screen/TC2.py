#Verify user has entered information in all fields
# Here we're checking by omitting blood group

from pickle import TRUE
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()  
driver.get("http://localhost:3000/register")  
inputElement = driver.find_element_by_id("first_name")
inputElement.send_keys('Tania')
time.sleep(3)  
inputElement = driver.find_element_by_id("phone")
inputElement.send_keys('9779918111')  
l = driver.find_element_by_name("register_btn")
l.click()  
time.sleep(5)  