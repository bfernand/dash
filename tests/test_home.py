import time

def test_home(browser):
    url = 'http://172.31.70.179:8080'
    browser.get(url)
    time.sleep(10)
    assert 'Dash' in browser.title, "O título da página não contém 'Dash'."
    assert 'pagina inicial' in browser.page_source, "O conteúdo da página não contém 'pagina inicial'."
