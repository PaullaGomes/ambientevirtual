from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



# Inicia o navegador Google Chrome
navegador = webdriver.Chrome()

navegador.get('https://selenium.dunossauro.live/aula_06_a.html')
sleep(6)
nome = navegador.find_element(By.CSS_SELECTOR,'input[name="nome"]').send_keys('Paulla Gomes')
senha = navegador.find_element(By.CSS_SELECTOR,'input[name="senha"]').send_keys('123456')
botao = navegador.find_element(By.CSS_SELECTOR,'input[name="10c0"]').click()
sleep(8)
