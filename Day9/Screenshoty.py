from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import time
import datetime
import calendar
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://www.redbus.in/")
driver.implicitly_wait(30)

#driver.save_screenshot("C:\\Cypress\\red_partial.jpg")
#driver.save_full_page_screenshot("C:\\Cypress\\red_ful.jpg")
print(datetime.datetime.now())
gmt = time.gmtime()
print(calendar.timegm(gmt))
driver.get_screenshot_as_file("screenshot_"+str(calendar.timegm(gmt))+".png")
driver.get_screenshot_as_png()
#print(driver.get_screenshot_as_png())


#driver.get_screenshot_as_base64()