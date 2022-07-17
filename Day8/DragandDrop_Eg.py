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

driver.get("https://jqueryui.com/droppable/")
driver.implicitly_wait(30)

driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@class="demo-frame"]'))

act = ActionChains(driver)
dragelement =driver.find_element(By.XPATH,"//div[@id='draggable']")
drpelement = driver.find_element(By.XPATH,"//div[@id='droppable']")
# #act.drag_and_drop(dragelement,drpelement)
# act.click_and_hold(dragelement)
# act.release(drpelement)

act.drag_and_drop_by_offset(dragelement,150,50)

act.perform()