import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
import time


@pytest.fixture()
def prestep():
    global driver
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield
    driver.close()
    print("called yield")

@pytest.mark.skip("simply skip")
def test_google(prestep):
    driver.get("https://www.google.com/")
    print(driver.title)
    print(driver.current_url)


def test_bing(prestep):
    driver.get("https://www.bing.com/")
    print(driver.title)
    print(driver.current_url)

def test_facebook(prestep):
    driver.get("https://www.facebook.com/")
    print(driver.title)
    print(driver.current_url)
    #self.assertEqual("Facebook",self.driver.title)
    #self.assertTrue("Facebook" == self.driver.title)

