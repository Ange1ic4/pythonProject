import email
from requests_html import HTMLSession
import requests
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup


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

url = "https://webmail-seguro.com.br/?_task=mail&_mbox=INBOX"
session = HTMLSession()
r = session.get(url)
r.html.link

data = r.html.find('.lm-panel-middle lm-list-panel')

assert isinstance(data, object)
print(data)

# sb = requests.get(site).text
# soup = BeautifulSoup(sb, 'html.parser')
# dia = soup.find_all(class_='date')

print()
time.sleep(5)


for l in linhas:
    data = l.find_element('class name', 'date')
    if data.text == "":
        print()
    else:
        ft = datetime.strptime(data.text, '%d/%m/%Y %H:%M')
        print(ft)
        print(data.text)