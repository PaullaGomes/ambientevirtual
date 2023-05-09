from selenium.webdriver import Chrome
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


# Inicia o navegador Google Chrome
navegador = webdriver.Chrome()

navegador.get('https://selenium.dunossauro.live/keyboard')
sleep(6)

html= navegador.find_element(By.TAG_NAME, 'html')
sleep(6)
html.send_keys('selenium') #send_keys envia o texto todo de uma só vez.
sleep(8)


