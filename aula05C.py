from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicia o navegador Google Chrome
navegador = webdriver.Chrome()

# Carrega a página que queremos automatizar
navegador.get('https://selenium.dunossauro.live/aula_05_c.html')

#Encontra e Preenche o formulário com nome do filme, email e telefone:
filme = navegador.find_element(By.NAME,'filme')
filme.send_keys('Parasita')
time.sleep(10)

email= navegador.find_element(By.NAME,'email')
email.send_keys('dudu@dudu.edu.com')
time.sleep(10)


telefone= navegador.find_element(By.NAME,'telefone')
telefone.send_keys("(11)916533232")
time.sleep(5)

#Clicar no botão enviar:
botao = navegador.find_element(By.NAME,'enviar').click()

input('')

