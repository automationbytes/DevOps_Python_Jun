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

driver.get("https://www.redbus.in/")
driver.implicitly_wait(30)

driver.find_element(By.ID,"onward_cal").click()
time.sleep(3)
#
# Monthtitle = driver.find_element(By.CLASS_NAME,"monthTitle").text
# print(Monthtitle)
#Dec
for i in range(12):
    driver.find_element(By.XPATH,"//button[text()='>']").click()
    time.sleep(2)
    Monthtitle = driver.find_element(By.CLASS_NAME, "monthTitle").text
    print(Monthtitle)
    if "Dec" in Monthtitle:

        dates = driver.find_elements(By.XPATH,'//table[@class="rb-monthTable first last"]//td')
        for d in dates:
            if "26" in d.text:
                d.click()
                break
        break