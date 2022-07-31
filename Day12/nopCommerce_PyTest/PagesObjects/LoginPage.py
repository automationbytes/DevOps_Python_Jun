from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:

    username_textbox_id = 'Email'
    password_textbox_id = 'Password'
    login_button_xpath = "//button[text()='Log in']"

    def __init__(self,driver):
        self.driver = driver

    def enterUserName(self,username):
        self.driver.findElement(By.ID,self.username_textbox_id).clear()
        self.driver.findElement(By.ID,self.username_textbox_id).sendKeys(username)

    def enterpassword(self, password):
        self.driver.findElement(By.ID, self.password_textbox_id).clear()
        self.driver.findElement(By.ID, self.password_textbox_id).sendKeys(password)

    def clickLogin(self):
        self.driver.findElement(By.XPATH,self.login_button_xpath).click()



