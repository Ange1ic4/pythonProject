from datetime import datetime, date
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
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

navegador.find_element('xpath', '//*[@id="lm-sidebar"]/div[4]/div[3]/div/span[2]').click()

seta = navegador.find_elements('id', 'rcmbtnnavlast')

count = 1


while count == 1:
    # Encontrar a tabela de emails
    linhas = navegador.find_elements('xpath', '/html/body/div[2]/main/section/div[1]/table/tbody/tr')
    print("Passou pelo while")
    print(len(linhas))
    # Encontrar a data dos emails de uma página e transformar em datetime
    for n in linhas:
        data = n.find_element('class name', 'date').text
        if data is None:
            print()
        else:
            ft = datetime.strptime(data, '%d/%m/%Y %H:%M')
            lim = datetime(year=2021, month=2, day=1, hour=0, minute=0, second=0)
        # Filtrando datas abaixo de 01/02/2021
            if ft < lim:
                print()
            else:
                count = count + 1

    # Selicionar tudo
    navegador.find_element('xpath', '//*[@id="lm-act-checkbox"]/label').click()

    # Mais
    navegador.find_element('id', 'rcmbtn117').click()

    # Mover para
    navegador.find_element('id', 'rcmbtn118').click()

    # Repositório
    navegador.find_element('xpath', '//*[@id="folder-selector"]/ul/li[31]/a').click()

    # Esperar a página carregar

    # navegador.find_element()
    while True:
        loading = navegador.find_elements('class name', 'loading')
        if len(loading) > 0:
            try:
                loading[0].is_displayed()
            except:
                pass

            continue

        break
print()
time.sleep(5)
