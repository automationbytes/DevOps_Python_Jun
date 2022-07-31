from DevOps_Python_Jun.Day12.POM_UnitTest.Locators.locators import  locators
from selenium import webdriver
from selenium.webdriver.common.by import By
class HomePage():
    def __init__(self,driver):
        self.driver = driver


    def click_WelcomeButton(self):
        self.driver.findElement(By.ID,locators.welcome_link_id).click()

    def clickLogout(self):
        self.driver.findElement(By.XPATH,locators.logout_link_xpath).click()
