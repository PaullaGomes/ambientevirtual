from selenium.webdriver.common.by import By 
from selenium import webdriver
from time import sleep
from abc import ABC
from selenium.webdriver import Chrome



class PageElement(ABC):
    def __init__(self, webdriver,url=''):
        self.webdriver = webdriver
        self.url = url

    def fin_element(self, locator):
         return self.webdriver.find_element(*locator)

    def fin_elements(self, locator):
         return self.webdriver.find_elements(*locator)

    def open(self, url):
          self.webdriver.get(self.url)

class Todo(PageElement):
        name = (By.ID, "todo-name")
        description = (By.ID,"todo-desc")
        urgent = (By.ID,"todo-next")
        submit= (By.ID,"todo-sumit")

        webdriver = webdriver

        sleep(5)

        def create_todo(self, name, description, urgent=False):
                self.webdriver.find_element(*self.name).send_keys(name)
                self.webdriver.find_element(*self.description).send_keys(description)
                if urgent:
                    self.webdriver.find_element(*self.urgent).click()
                self.webdriver.find_element(*self.submit).click()         


        sleep(5)

class CardContainer( PageElement,ABC):
     def todos(self):
        cards= self.find_elements(self.card)
        po_cards= []
        for card in cards:
             po_cards.append(Card(card))

        return po_cards


class AFazer(CardContainer):
    fieldset=(By.CSS_SELECTOR,'div.body_a fieldset')
    card = (By.CLASS_NAME, 'terminal-card')

class Fazendo(CardContainer):
    fieldset=(By.CSS_SELECTOR,'div.body_b fieldset')
    card = (By.CLASS_NAME, 'terminal-card')


class Pronto(CardContainer):
    fieldset=(By.CSS_SELECTOR,'div.body_c fieldset')
    card = (By.CLASS_NAME, 'terminal-card')

    def todos(self):
        cards= self.find_elements(self.card)
        po_cards= []
        for card in cards:
             po_cards.append(Card(card))

        return po_cards
    
class Card:
     def __init__(self,selenium_object):
          self.selenium_object= selenium_object
          self.name = By.CSS_SELECTOR,'header.name'
          self.description = By.CSS_SELECTOR,'div.description'  
          self.__do = By.CSS_SELECTOR,"button.do"
          self.__cancel = By.CSS_SELECTOR,"button.cancel"
          self._load()

     def do(self):
          self.selenium_object.find_element(self._do).click()

     def cancel(self):
          self.selenium_object.find_element(self.__cancel).click()
     
     def load(self):
          self.name= self.selenium_object.find_element(*self.name).text
          self.description= self.selenium_object.find_element(*self.description).text
          
     def __repr__(self):
          return f'Card(name="{self.name}", description = "{self.description}")'

sleep(5)

webdriver= Chrome()
url = 'https://selenium.dunossauro.live/todo_list.html'

sleep(5)

todo_element= Todo(webdriver,url)
todo_element.open(url)

sleep(5)

todo_element.create_todo(
    name = 'Dormir',
    description ='Dormir é muito bom'
)

sleep (25)
a_fazer = AFazer(webdriver)

todos = a_fazer.todos()

sleep (25)
todos[0].do()
#todos[0].cancel()

fazendo = Fazendo(webdriver)
print (fazendo.todos())
sleep (50)

