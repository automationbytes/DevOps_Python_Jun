from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
import time
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.XPATH,'//input[@name="txtUsername"]').send_keys("Admin")
driver.find_element(By.XPATH,'//input[@name="txtPassword"]').send_keys("admin123")
driver.find_element(By.XPATH,'//input[@value="LOGIN"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//b[text()="Recruitment"]').click()

jobTitledrpdwn = Select(driver.find_element(By.XPATH,'//select[@id="candidateSearch_jobTitle"]'))
jobTitledrpdwn.select_by_index(10)

statusdrpdwn = Select(driver.find_element(By.XPATH,'//select[@id="candidateSearch_status"]'))
statusdrpdwn.select_by_value("INTERVIEW PASSED")
time.sleep(8)
jobTitledrpdwn.select_by_visible_text("QA Lead")

for j in jobTitledrpdwn.options:
    print(j.text)