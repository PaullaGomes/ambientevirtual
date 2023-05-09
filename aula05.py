from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Inicia o navegador Google Chrome
navegador = webdriver.Chrome()

# Carrega a página que queremos automatizar
navegador.get('https://selenium.dunossauro.live/aula_05.html')

#Encontra e Preenche o formulário com nome, email, senha e telefone:

nome = navegador.find_element(By.NAME,'nome')
nome.send_keys('Paulla Gomes')
sleep(10)

email= navegador.find_element(By.NAME,'email')
email.send_keys('paullagomes332@gmail.com')
sleep(10)

senha= navegador.find_element(By.NAME,'senha')
senha.send_keys('123456')
sleep(10)

telefone= navegador.find_element(By.NAME,'telefone')
telefone.send_keys('11-916533232')
sleep(5)

botao = navegador.find_element(By.NAME,'btn').click()
sleep(10)   


input('')
