from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import time
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

#page load time out - used for launching websites
driver.set_page_load_timeout(60)
driver.get("https://www.irctc.co.in/nget/train-search")

#used for all the elements
driver.implicitly_wait(30)
#time.sleep(30)
#
# #for particular element
# wait = WebDriverWait(driver,15)
# wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[text()='OK']")))
# driver.find_element(By.XPATH,"//button[text()='OK']").click()


#fluent wait

wait = WebDriverWait(driver,15,poll_frequency=3,ignored_exceptions="NoSuchElementException")
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[text()='OK']")))
driver.find_element(By.XPATH,"//button[text()='OK']").click()
