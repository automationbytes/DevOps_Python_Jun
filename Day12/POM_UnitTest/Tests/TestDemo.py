from selenium import webdriver
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from DevOps_Python_Jun.Day12.POM_UnitTest.Pages.loginPage import LoginPage
from DevOps_Python_Jun.Day12.POM_UnitTest.Pages.homePage import HomePage
from HTMLTestRunner.runner import HTMLTestRunner
import sys
import os
#sys.path.append(os.path.dirname(__file__),"..","..")





class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")


    def test_1_Login(self):
        login = LoginPage(self.driver)
        login.enterUserName("Admin")
        login.enterPassword("admin123")
        login.clickLogin()

    def test_2_Logout(self):
        homePage = HomePage(self.driver)
        #homePage.click_WelcomeButton()
        homePage.clickLogout()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    if __name__ == '__main__':
        runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                                open_in_browser=True, description="HTMLTestReport", tested_by="Devops university",
                                add_traceback=False)
