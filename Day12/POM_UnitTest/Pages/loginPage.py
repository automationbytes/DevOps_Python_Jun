from DevOps_Python_Jun.Day12.POM_UnitTest.Locators.locators import locators
from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        # self.username_textbox_xpath = '//input[@name="txtUsername"]'
        # self.password_textbox_xpath = '//input[@name="txtPassword"]'
        # self.login_button_xpath = '//input[@name="Submit"]'

    def enterUserName(self,UserName):
        self.driver.find_element(By.XPATH,locators.username_textbox_xpath).send_keys(UserName)


    def enterPassword(self,Password):
        self.driver.find_element(By.XPATH, locators.password_textbox_xpath).send_keys(Password)


    def clickLogin(self):
        self.driver.find_element(By.XPATH,locators.login_button_xpath).click()
