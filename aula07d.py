from selenium.webdriver import Chrome
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By



# Inicia o navegador Google Chrome
navegador = webdriver.Chrome()

navegador.get('https://selenium.dunossauro.live/aula_07_d.html')
sleep(6)


texto= navegador.find_element(By.TAG_NAME,'input')
span = navegador.find_element(By.TAG_NAME,'span')
p = navegador.find_element(By.TAG_NAME,'p')

sleep(6)


texto.click()
#"assert" para verificar se o resultado esperado é produzido pelo código.
assert 'está com foco' == span.text, 'esta com foco não está em span'
span.click()
assert 'esta sem foco' ==span.text, 'esta semfoco não está em span'

assert p.text == "0", 'p não é zero'
texto.send_keys('batata')
assert 'esta com foco' == span.text, "esta com foco nao esta em span"
span.click()

assert 'esta sem foco' == span.text, "esta sem foco nao esta em span"
span.click()
assert p.text == "1", 'p não é um'

sleep(25)


