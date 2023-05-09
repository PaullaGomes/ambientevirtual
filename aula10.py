from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
driver.get("https://cursoautomacao.netlify.app/desafios.html")
sleep(1)
#endereço da janela atual:
janela_inicial = driver.current_window_handle
driver.execute_script('window.scrollTo(0,2500)')
sleep(1)
botao_abrir_nova_janela = driver.find_element(
    By.XPATH, "//button[text()='Abrir nova janela']")
driver.execute_script('arguments[0].click()', botao_abrir_nova_janela)
janelas = driver.window_handles
#Laço de repetição:
for janela in janelas:
    if janela not in janela_inicial:
        sleep(1)
        driver.switch_to.window(janela)
        campo_opiniao = driver.find_element(By.ID, 'opiniao_sobre_curso')
        sleep(1)
        campo_opiniao.send_keys('Curso muito TOP!')
        sleep(9)
        botao_pesquisar = driver.find_element(By.ID, "fazer_pesquisa")
        sleep(5)
        botao_pesquisar.click()
        sleep(3)
        driver.close()

driver.switch_to.window(janela_inicial)
campo = driver.find_element(By.ID, "campo_desafio7")
campo.send_keys('Voltando...1...2...3...4 UhUuUuUuU!')


input('')
driver.close()