import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://accounts.saucelabs.com/am/XUI/#login/")
driver.maximize_window()
time.sleep(5)
checkbox_status = driver.find_element(By.XPATH,'//input[@name="loginRemember"]').is_selected()
print(checkbox_status)
driver.find_element(By.XPATH,'//input[@name="loginRemember"]').click()
checkbox_status = driver.find_element(By.XPATH,'//input[@name="loginRemember"]').is_selected()
print(checkbox_status)