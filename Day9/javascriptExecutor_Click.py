from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import time
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.implicitly_wait(30)
time.sleep(5)
driver.execute_script("arguments[0].click();",driver.find_element(By.XPATH,"//a[text()=' BUSES ']"))

