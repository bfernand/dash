import pytest
import time
from selenium import webdriver



chrome_path = '/home/bruno/aula-python/scripting/chrome-linux64/chrome'
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

url = 'http://172.31.70.179:8080' 

driver.get(url)
time.sleep(10)
assert 'Dash' in driver.title, "O título da página não contém 'Dash'."
assert 'pagina inicial' in driver.page_source, "O conteúdo da página não contém 'pagina inicial'."
print("Teste da pagina inicial com sucesso!")

driver.get(url + '/formulario')
time.sleep(10)
assert 'Dashboard - Formulario' in driver.title, "O título da página não contém 'Dashboard - Formulario'."
assert 'Formulario' in driver.page_source, "O conteúdo da página não contém 'Formulario'."
print("Teste da pagina do formulario com sucesso!")
    
driver.get(url + '/graficos')
time.sleep(10)
assert 'Dashboard - Graficos' in driver.title, "O título da página não contém 'Dashboard - Graficos'."
assert 'Graficos' in driver.page_source, "O conteúdo da página não contém 'Graficos'."
print("Teste da pagina de graficos com sucesso!")

driver.quit()