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

driver.get("https://www.toyota.co.uk/order-a-brochure")
driver.implicitly_wait(30)
try:
    driver.find_element(By.XPATH,"//button[@id='onetrust-accept-btn-handler']").click()
except:
     pass
# driver.find_element(By.XPATH,"//a[@aria-label='Help Centre']").click()
# driver.back()
time.sleep(5)
driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@title="Order a Brochure"]'))
time.sleep(5)
driver.find_element(By.XPATH,'//a[@href="#download"]').click()