from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.facebook.com/")
driver.maximize_window()
# driver.find_element(By.ID,"email").send_keys("username")
# driver.find_element(By.NAME,"pass").send_keys("password123")
# #When provided id/name is not crrt, ti will return no such element exceptin
# driver.find_element(By.PARTIAL_LINK_TEXT,"Forgotten pass").click()


driver.find_element(By.XPATH, '//input[@data-testid="royal_email"]').send_keys("hello")