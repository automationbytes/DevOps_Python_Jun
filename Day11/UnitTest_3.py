import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
import time

class LaunchURL(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.maximize_window()

    def test_google(self):
        self.driver.get("https://www.google.com/")
        print(self.driver.title)
        print(self.driver.current_url)


    def test_bing(self):
        self.driver.get("https://www.bing.com/")
        print(self.driver.title)
        print(self.driver.current_url)


    def test_facebook(self):
        self.driver.get("https://www.facebook.com/")
        print(self.driver.title)
        print(self.driver.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

def suite():
    suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(LaunchURL)) # to add all
    suite.addTest(LaunchURL("test_facebook")) # add specific case
    return suite
if __name__ == '__main__':
    #unittest.main()
    runner = unittest.TextTestRunner()
    testsuite = suite()
    runner.run(testsuite)
