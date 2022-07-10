from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://www.leafground.com/pages/radio.html")
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@value="0" and @name="news"]').click()
radiostatus = driver.find_element(By.XPATH,'//input[@value="0" and @name="news"]').is_selected()
print(radiostatus)


numberofradiobtns = driver.find_elements(By.XPATH,'//input[@name="news"]')
print(type(numberofradiobtns))

print(len(numberofradiobtns))
