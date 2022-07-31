import pytest
from selenium import webdriver
from DevOps_Python_Jun.Day12.nopCommerce_PyTest.PagesObjects.LoginPage import LoginPage
from DevOps_Python_Jun.Day12.nopCommerce_PyTest.PagesObjects.HomePage import HomePage
from DevOps_Python_Jun.Day12.nopCommerce_PyTest.Config.PropReader import PropReader

class TestLogin:
        '''
        py - how we stored locators in earlier unit test framework
        config.property -
        '''

        baseUrl = PropReader.readProp("url")

        def test_1_login(self,setup):
                driver = webdriver.Chrome()

                self.driver = setup
                self.driver.get(self.baseUrl)
                self.driver.maximize_window()
                self.driver.implicitly_wait(30)

                lp = LoginPage(self.driver)
                lp.enterUserName(PropReader.readProp("username"))
                lp.enterpassword(PropReader.readProp("password"))
                lp.clickLogin()

        def test_2_login(self, setup):
                hp = HomePage(self.driver)
                if hp.dashboard_header_xpath == True:
                        assert True
                else:
                        self.driver.save_screenshot(".\\screenshots\\dashboard.png")
                        assert False