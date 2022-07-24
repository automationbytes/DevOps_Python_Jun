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
#
# for i in range(1,rows):
#     candidatename = driver.find_element(By.XPATH,'//table[@id="resultTable"]//tr['+str(i)+']/td[3]/a')
#     print(candidatename.text)
#     if candidatename.text == 'Mason Jenson':
#         driver.find_element(By.XPATH,'//table[@id="resultTable"]//tr['+str(i)+']/td[1]/input').click()
#         break
selectedcandidates = []
for i in range(1,rows):
    status = driver.find_element(By.XPATH,'//table[@id="resultTable"]//tr['+str(i)+']/td[6]')
    print(status.text)
    if status.text == 'Shortlisted':
        driver.find_element(By.XPATH, '//table[@id="resultTable"]//tr[' + str(i) + ']/td[1]/input').click()
        candidatename = driver.find_element(By.XPATH, '//table[@id="resultTable"]//tr[' + str(i) + ']/td[3]/a').text
        selectedcandidates.append(candidatename)

print(selectedcandidates)