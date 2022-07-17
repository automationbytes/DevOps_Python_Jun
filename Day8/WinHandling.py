from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import time
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://www.openmultipleurl.com/")
driver.implicitly_wait(30)
driver.find_element(By.XPATH,'//textarea[@name="list_urls"]').send_keys("https://www.google.com/")
driver.find_element(By.XPATH,'//textarea[@name="list_urls"]').send_keys(Keys.ENTER)

driver.find_element(By.XPATH,'//textarea[@name="list_urls"]').send_keys("https://www.facebook.com/")
driver.find_element(By.XPATH,'//textarea[@name="list_urls"]').send_keys(Keys.ENTER)

driver.find_element(By.XPATH,'//textarea[@name="list_urls"]').send_keys("https://www.yahoo.com/")
driver.find_element(By.XPATH,'//textarea[@name="list_urls"]').send_keys(Keys.ENTER)

driver.find_element(By.XPATH,'//textarea[@name="list_urls"]').send_keys("https://www.amazon.com/")
driver.find_element(By.XPATH,'//textarea[@name="list_urls"]').send_keys(Keys.ENTER)


driver.find_element(By.XPATH,'//textarea[@name="list_urls"]').send_keys("https://www.bing.com/")
driver.find_element(By.XPATH,'//textarea[@name="list_urls"]').send_keys(Keys.ENTER)

driver.find_element(By.XPATH,'//input[@value="Go Now"]').click()

print(driver.title)
print(driver.current_url)
parentwindow = driver.current_window_handle
print(parentwindow)
allopenwindows = driver.window_handles #this includes parent window also
print(allopenwindows)
print(len(allopenwindows))
print(type(allopenwindows))#list
time.sleep(10)
for a in allopenwindows:
    if a != parentwindow:
        time.sleep(5)
        driver.switch_to.window(a)
        print(driver.current_url)
        if 'Bing' in driver.title:
            driver.find_element(By.XPATH,'//input[@name="q"]').send_keys("Selenium")
            driver.find_element(By.XPATH,'//input[@name="q"]').send_keys(Keys.ENTER)

            time.sleep(15)
        else:
            driver.close()

driver.switch_to.window(parentwindow)

