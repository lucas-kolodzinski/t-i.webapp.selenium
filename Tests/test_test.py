#REFERENCE TEST FILE - Will be deleted in future

from selenium import webdriver
import unittest
import allure
from time import sleep

driver = webdriver.Firefox()
driver.set_page_load_timeout(20)
driver.get("http://the-internet.herokuapp.com/")
sleep(2)
print(driver.title)
driver.maximize_window()
driver.get_screenshot_as_file("/home/lucas/SELENIUM/t-i.webapp.selenium/Screenshots/home_page.png")
driver.implicitly_wait(10)
driver.close()
driver.quit()