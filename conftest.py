import pytest
import time
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    #chrome_path = '/home/bruno/aula-python/scripting/chrome-linux64/chrome'
    #chrome_options.binary_location = chrome_path
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--user-data-dir=/tmp/chrome-profile')
    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()