from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

def test_open_parabank():
    driver = webdriver.Firefox()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    assert "ParaBank" in driver.title
    time.sleep(3)
    driver.quit()

