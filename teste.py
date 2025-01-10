import pytest
import time
from selenium import webdriver

url = 'http://172.31.70.179:8080'

@pytest.fixture
def driver():
    chrome_path = '/home/bruno/aula-python/scripting/chrome-linux64/chrome'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.binary_location = chrome_path
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()    

def test_pagina_inicial(driver):
    driver.get(url)
    time.sleep(10)
    assert 'Dash' in driver.title, "O título da página não contém 'Dash'."
    assert 'pagina inicial' in driver.page_source, "O conteúdo da página não contém 'pagina inicial'."

def test_pagina_formulario(driver):
    driver.get(url + '/formulario')
    time.sleep(10)
    assert 'Dashboard - Formulario' in driver.title, "O título da página não contém 'Dashboard - Formulario'."
    assert 'Formulario' in driver.page_source, "O conteúdo da página não contém 'Formulario'."
    
def test_pagina_graficos(driver):
    driver.get(url + '/graficos')
    time.sleep(10)
    assert 'Dashboard - Graficos' in driver.title, "O título da página não contém 'Dashboard - Graficos'."
    assert 'Graficos' in driver.page_source, "O conteúdo da página não contém 'Graficos'."