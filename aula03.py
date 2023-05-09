from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse


# Inicia o navegador Google Chrome
navegador = webdriver.Chrome()

navegador.get('https://selenium.dunossauro.live/exercicio_03.html')

sleep(6)

#pagina inicial
main = navegador.find_element(By.TAG_NAME,'main')
clique_aqui = main.find_element(By.TAG_NAME,'a')
clique_aqui.click()
sleep(6)

#pagina 1
elementos = navegador.find_elements(By.TAG_NAME,'a')
elemento_errado = [elemento for elemento in elementos if elemento.get_attribute('attr') == 'errado']
elemento_errado[0].click()

sleep(6)

#pagina 2
navegador.refresh() #se nao der refresh nao aparece nada
elementos = navegador.find_elements(By.TAG_NAME,'a')
elemento_certo = [elemento for elemento in elementos if elemento.text == navegador.title]
elemento_certo[0].click()

sleep(6)

#pagina 3

elementos = navegador.find_elements(By.TAG_NAME,'a')
elemento_certo = [elemento for elemento in elementos if urlparse(elemento.get_attribute('href')).path == "/page_4.html"]
elemento_certo[0].click()

sleep(6)
#pagina 4
navegador.refresh()
#Você ganhou

sleep(6)