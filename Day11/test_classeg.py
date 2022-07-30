import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class lanchbrowser():
    @pytest.fixture()
    def prestep(self):
      #  global self.driver
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()
        print("called yield")

    @pytest.mark.skip("simply skip")
    def test_google(self,prestep):
        self.driver.get("https://www.google.com/")
        print(self.driver.title)
        print(self.driver.current_url)

    def test_bing(self,prestep):
        self.driver.get("https://www.bing.com/")
        print(self.driver.title)
        print(self.driver.current_url)

    def test_facebook(self,prestep):
        self.driver.get("https://www.facebook.com/")
        print(self.driver.title)
        print(self.driver.current_url)
        # self.assertEqual("Facebook",self.self.driver.title)
        # self.assertTrue("Facebook" == self.self.driver.title)

