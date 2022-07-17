from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import time
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.implicitly_wait(30)

driver.find_element(By.XPATH,'//a[@onclick="retheme()"]').click()
driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH,"//button[text()='Try it']").click()

driver.switch_to.alert.send_keys("Tom")
driver.switch_to.alert.accept()

driver.switch_to.default_content()
driver.find_element(By.XPATH,'//a[@onclick="retheme()"]').click()