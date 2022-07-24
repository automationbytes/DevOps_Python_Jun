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

#find the row
rows = len(driver.find_elements(By.XPATH,'//table[@id="resultTable"]//tr'))
print(rows)

#find the column
col = len(driver.find_elements(By.XPATH,'//table[@id="resultTable"]//th'))
print(col)

for c in range(1,col+1):
    header = driver.find_element(By.XPATH,'//table[@id="resultTable"]//th['+str(c)+']/*')
    print(header.text)
    if header.text == 'Candidate': #wat is column
        for r in range(1, rows):
         candidatename = driver.find_element(By.XPATH,'//table[@id="resultTable"]//tr['+str(r)+']/td['+str(c)+']/a')
         print(candidatename.text)

