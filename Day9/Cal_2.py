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
driver.find_element(By.ID,"candidateSearch_fromDate").click()

month = driver.find_element(By.CLASS_NAME,"ui-datepicker-month")
m = Select(month)
m.select_by_visible_text("Dec")

time.sleep(2)
year = driver.find_element(By.CLASS_NAME,"ui-datepicker-year")
y = Select(year)
y.select_by_visible_text("2020")

day = driver.find_elements(By.XPATH,'//table[@class="ui-datepicker-calendar"]//a')
for d in day:
    print(d.text)
    if d.text == "19":
        d.click()
        break