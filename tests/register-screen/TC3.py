#Verify user can only enter valid blood group

from pickle import TRUE
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()  
driver.get("http://localhost:3000/register")  
l = driver.find_element_by_name("blood")
l.click()  
time.sleep(5)  