from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


def aguarda_elemento(tipo, id):
    botao = navegador.find_elements(tipo, id)
    while len(botao) == 0:
        botao = navegador.find_elements(tipo, id)


navegador = webdriver.Chrome()

# encontrar o campo "email" e preencher
navegador.get('https://webmail-seguro.com.br/bauheradvogados.adv.br/')

navegador.find_element('id', "rcmloginuser").send_keys("giovanna@bauheradvogados.adv.br")

# encontrar o campo "senha" e preencher
navegador.find_element('id', "rcmloginpwd").send_keys("TempP@ss123")
navegador.find_element('id', "submitloginform").click()
aguarda_elemento('id', "close-popover")

navegador.find_element('id', "close-popover").click()

seta = navegador.find_elements('id', 'rcmbtnnavlast')

while len(seta) == 1:
# Selicionar tudo
    navegador.find_element('xpath', '//*[@id="lm-act-checkbox"]/label').click()

# Mais
    navegador.find_element('id', 'rcmbtn117').click()

# Mover para
    navegador.find_element('id', 'rcmbtn118').click()

# Repositório
    navegador.find_element('xpath', '//*[@id="folder-selector"]/ul/li[31]/a').click()

    while True:
        loading = navegador.find_elements('class name', 'loading')
        if len(loading) > 0:
            try:
                loading[0].is_displayed()
            except:
                pass

            continue

        break

    seta = navegador.find_elements('id', 'rcmbtnnavlast')

time.sleep(5)
print()
print()