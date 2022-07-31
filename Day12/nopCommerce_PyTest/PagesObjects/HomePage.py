

from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:

    dashboard_header_xpath = "//h1[contains(text(),'Dashboard')]"
    logout_button_xpath = "//a[text()='Logout']"

    def __init__(self,driver):
        self.driver = driver


    def verifydashboardHeader(self):
        return self.driver.findElement(By.XPATH,self.dashboard_header_xpath).is_displayed()

    def clickLogout(self):
        self.driver.findElement(By.XPATH,self.logout_button_xpath).click()

