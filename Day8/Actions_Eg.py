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

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.implicitly_wait(30)
act = ActionChains(driver)
#rightclick - context click
act.context_click(driver.find_element(By.XPATH,"//span[text()='right click me']"))
act.move_to_element(driver.find_element(By.XPATH,"//span[text()='Copy']"))
act.click(driver.find_element(By.XPATH,"//span[text()='Copy']"))
act.perform()

driver.switch_to.alert.accept()

#double click
act.double_click(driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']")).perform()

driver.switch_to.alert.accept()