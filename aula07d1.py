from selenium.webdriver import Chrome
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.events import (AbstractEventListener, EventFiringWebDriver)
from selenium.webdriver.common.by import By

# Define a classe Escuta, que herda de AbstractEventListener.
class Escuta(AbstractEventListener):
#Define o método before_click, que é chamado antes de um clique em um elemento.
    def before_click(self, elemento, webddriver):
        print('Antes do clique')

#Define o método after_click, que é chamado depois de um clique em um elemento.
    def after_click(self, elemento, webdrdriver):
        print('Depois do clique')

        

# A partir daqui, o código cria uma instância do navegador Chrome e uma instância de EventFiringWebDriver, que é usada para monitorar eventos no navegador.
navegador = webdriver.Chrome()

#Cria uma instância de EventFiringWebDriver, que monitora eventos no navegador. É passado o navegador criado anteriormente e uma instância da classe Escuta.
rapi_10= EventFiringWebDriver(navegador, Escuta())

rapi_10.get('https://selenium.dunossauro.live/aula_07_d.html')
sleep(6)

#Localiza os elementos:
texto= rapi_10.find_element(By.TAG_NAME,'input')
span = rapi_10.find_element(By.TAG_NAME,'span')
p = rapi_10.find_element(By.TAG_NAME,'p')

texto.click()


