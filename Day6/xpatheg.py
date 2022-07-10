from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@id="txtUsername"]').clear()
driver.find_element(By.XPATH,'//input[@id="txtUsername"]').send_keys("Admin")
driver.find_element(By.XPATH,'//input[@id="txtPassword"]').clear()
driver.find_element(By.XPATH,'//input[@id="txtPassword"]').send_keys("admin123")
#driver.find_element(By.XPATH,'//input[@value="LOGIN"]').click()