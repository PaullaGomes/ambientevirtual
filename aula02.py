
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import re



# Inicia o navegador Google Chrome
browser = webdriver.Chrome()
# Carrega a página que queremos automatizar
browser.get('https://curso-python-selenium.netlify.app/exercicio_02.html')
sleep(5)

#Encontre a TAG a:
link = browser.find_element(By.TAG_NAME,'a')

#Criando loop com condicional para retornar todos os 'p',
# pegando o último elemento da lista p e armazenando essa mensagem na variável p1.
# O padrão de busca é \\bVocê ganhou\\b,que procura pela string exata "Você ganhou"
#  
while True:
    link.click()
    p = browser.find_elements(By.TAG_NAME,'p')
    p1 = p[-1].text
    if re.search('\\bVocê ganhou\\b', p1, re.IGNORECASE):
        break

sleep(10)
    