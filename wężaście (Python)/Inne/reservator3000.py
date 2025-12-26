from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("http://selenium.dev")
sleep(10)
driver.quit()