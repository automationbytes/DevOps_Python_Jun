import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture()
def setup(browser):
    if browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    return driver

def pytest_addoption(parser):
    parser.addoption(
        "--browser", help="Broswer: firefox or chrome"
    )


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")