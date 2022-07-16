from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
import time
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://www.redbus.in/")
driver.find_element(By.ID,"src").send_keys("kol")
time.sleep(5)
fromdrpdwn = driver.find_elements(By.XPATH,'//ul[@class="autoFill homeSearch"]//li')
for f in fromdrpdwn:
    #print(f.text)
    if "Airport" in f.text:
        f.click()
        break

###to drop
driver.find_element(By.ID,"dest").send_keys("sa")
time.sleep(2)
todrpdown = driver.find_elements(By.XPATH,'//ul[@class="autoFill homeSearch"]/li')
for t in todrpdown:
    print(t.text)
    if "Sathyamangalam" == t.text:
        t.click()
        break