
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

txtQ = (By.NAME, "q")

@pytest.fixture
def setUp():
    # drv = webdriver.ie("..//IEDriverServer.exe")
    return ""


def test_google_search(setUp):
    drv = webdriver.Chrome("..//chromedriver.exe")
    drv.get("https://www.google.com/")
    txt = drv.find_element(*txtQ)
    txt.send_keys("Solano County")

