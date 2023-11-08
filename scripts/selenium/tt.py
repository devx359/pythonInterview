import time
# import pytest
from selenium import webdriver

driver = webdriver.Chrome()

def test_setup():

    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    time.sleep(3)


def test_teardown():
    driver.quit()