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

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(30)

driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.NAME,"txtPassword").send_keys("admin123")
driver.find_element(By.NAME,"Submit").click()

Act = ActionChains(driver)
Act.move_to_element(driver.find_element(By.ID,"menu_admin_viewAdminModule"))
Act.move_to_element(driver.find_element(By.ID,"menu_admin_Organization"))
Act.move_to_element(driver.find_element(By.ID,"menu_admin_viewOrganizationGeneralInformation"))
Act.click(driver.find_element(By.ID,"menu_admin_viewOrganizationGeneralInformation")).perform()