from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
import time
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://www.leafground.com/pages/Alert.html")
driver.implicitly_wait(30)

driver.find_element(By.XPATH,"//button[text()='Alert Box']").click()
time.sleep(10)


#driver.find_element(By.XPATH,"//button[text()='Alert Box']").click()
driver.switch_to.alert.accept()

print(driver.switch_to.alert.text)
