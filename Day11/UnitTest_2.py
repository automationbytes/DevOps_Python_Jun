import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
import time

class LaunchURL(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()

   # @unittest.skip("Dont want to run")
  #  @unittest.skipIf(1 == 1,"Skip if the condition is true")
    @unittest.skipUnless(1 != 1,"skip if condition is false")
    def test_google(self):
        self.driver.get("https://www.google.com/")
        print(self.driver.title)
        print(self.driver.current_url)


    def test_bing(self):
        self.driver.get("https://www.bing.com/")
        print(self.driver.title)
        print(self.driver.current_url)
        self.assertEqual("Facebook", self.driver.title)

    @unittest.expectedFailure
    def test_facebook(self):
        self.driver.get("https://www.facebook.com/")
        print(self.driver.title)
        print(self.driver.current_url)
        #self.assertEqual("Facebook",self.driver.title)
        #self.assertTrue("Facebook" == self.driver.title)
        self.assertIn("Facebook",self.driver.title)
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()