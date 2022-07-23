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
driver.get("https://www.redbus.in/")
driver.implicitly_wait(30)
# #scroll using pixel values
# driver.execute_script("window.scrollBy(0,500);")
# time.sleep(10)
# driver.execute_script("window.scrollBy(0,500);")
#
# time.sleep(10)
# driver.execute_script("window.scrollBy(0,-750);")
#

#scrllTo
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

time.sleep(5)
phnnum = driver.find_element(By.XPATH,'//input[@id="smsTXTBOX"]')
driver.execute_script("arguments[0].scrollIntoView(true);",phnnum)
