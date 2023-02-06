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


def wait_load(navegador):
    while True:
        loading = navegador.find_elements('xpath', '/html/body/div[3]/div/div[2]/div')
        if len(loading) > 0:
            try:
                loading[0].is_displayed()
            except:
                pass

            continue

        break


class Processo:
    def __init__(self):
        pass

    def cabecalho(self):
       # numprocesso = navegador.find_elements('xpath', '//*[@id="app"]/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div/h3/span')
       # detalhes = navegador.find_elements('xpath', '/html/body/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/table')

        print("Cabeçalho")
        #for num in numprocesso:
        #    print(num.text)

      #  for det in detalhes:
     #       print(det.text)

    def fases(self):
        print("Fases")
        #navegador.execute_script('tabs = document.getElementsByClassName("tab-pane"); for (const tab of tabs) {tab.classList.remove("active"); }; document.getElementById("tabFases").classList.add("active");')
        #fases = navegador.find_elements('xpath', '/html/body/div/div/div[1]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div')

        #print("Fases")
        #for fase in fases:
          #  print(fase.text)

    def partadvs(self):
        print("Partes/Advogados")
        #navegador.execute_script('tabs = document.getElementsByClassName("tab-pane"); for (const tab of tabs) {tab.classList.remove("active"); }; document.getElementById("tabPartes").classList.add("active");')
        #partadvs = navegador.find_elements('xpath', '/html/body/div/div/div[1]/div/div/div[1]/div/div[2]/div/div/div/div/div[4]/div/table')
        #print("Partes/Advogados")

        #for partadv in partadvs:
         #   print(partadv.text)

navegador = webdriver.Chrome()

# Entrar no site
navegador.get('https://cpe.web.stj.jus.br/#/')

navegador.find_element('xpath', '//*[@id="app"]/div/div[2]/div[1]/div[1]/button').click()

aguarda_elemento('id', "q")

processos = ("00008437020158210133", "10036986220208260077", "81681311220228050001", "10858905120188260100")

for processo in processos:

    # Preencher o número do processo
    navegador.find_element('id', "q").send_keys(processo)

    # Clicar em pesquisar
    navegador.find_element('id', "search-btn").click()

    wait_load(navegador)
    time.sleep(5)
    nao_encontrado = navegador.find_elements('xpath', '//*[@id="app"]/div/div[2]/div')

    #Processo não encontrado
    if len(nao_encontrado) != 0:
        print("NENHUM PROCESSO ENCONTRADO.")
        #navegador.find_element('xpath', '/html/body/div/div/div[2]/div/div/div[3]/button').click() # problema
        navegador.find_element('id', "q").clear()
        #informe = navegador.find_elements('xpath', '//*[@id="app"]/div/div[2]/div')

        #if len(informe) != 0:

         #   navegador.find_element('xpath', '//*[@id="app"]/div/div[2]/div/div/div[3]/button').click()
        continue

    print(processo)
    proc = Processo()
    proc.cabecalho()
    proc.fases()
    proc.partadvs()

    navegador.find_element('id', "q").clear()




