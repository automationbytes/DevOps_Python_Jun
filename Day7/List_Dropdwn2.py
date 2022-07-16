from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
import time
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://www.goibibo.com/bus")
driver.find_element(By.XPATH,'//input[@aria-labelledby="downshift-1-label"]').send_keys("ban")
time.sleep(3)
listdropdwn = driver.find_elements(By.XPATH,'//div[@role="option"]//span')
for l in listdropdwn:
    print(l.text)