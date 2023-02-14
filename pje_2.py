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


def wait_load(tipo, id):
    while True:
        loading = navegador.find_elements(tipo, id)
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

    def primeirosite(self):
        processos = ("0807809-74.2017.4.05.8200", "0809066-37.2017.4.05.8200", "0899754-35.2020.4.05.8201", "0800754-35.2018.4.05.8201")

        # Entrar no site
        navegador.get('https://pje.jfpb.jus.br/pje/login.seam')

        aguarda_elemento('id', 'btnUtilizarApplet')

        navegador.execute_script('document.getElementById("btnUtilizarApplet").click()')

        while True:
            fechar = navegador.find_elements('xpath', "/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td/table/tbody")
            print(len(fechar))
            if (len(fechar)) == 0:
                print("Executou o if")
                continue
            else:
                navegador.execute_script('document.getElementById("btnfechar").click()')
                print("Executou o else")
               pass
            break

        navegador.find_element('id', "loginAplicacaoButton").click()

        aguarda_elemento('xpath', '//*[@id="validadeCertificadoModalContentTable"]/tbody/tr/td')

        navegador.get('https://pje.jfpb.jus.br/pje/Processo/ConsultaProcessoTerceiros/listView.seam')

        aguarda_elemento('id', "formValidadeCertificado:modalValidadeCertificadoDigital")

        navegador.find_element('xpath', '//*[@id="validadeCertificadoModalhidelink"]').click()

        for processo in processos:
            # Primeiro site

            print("Entrou no for primeiro site.")

            #navegador.find_element('id', 'pesquisarProcessoTerceiroForm:nrProcessoDecoration:nrProcesso').send_keys(processo)

            #navegador.execute_script('document.getElementById("pesquisarProcessoTerceiroForm:nrProcessoDecoration:nrProcesso").value = processo;')

            #navegador.execute_script('document.getElementById("pesquisarProcessoTerceiroForm:searchButton").click()')

            #navegador.find_element('id', "pesquisarProcessoTerceiroForm:searchButton").click()

            #wait_load('xpath', '//*[@id="modalStatusContentTable"]/tbody/tr/td')

            #detalhes = navegador.find_elements('id', "consultaProcessoTerceirosList:0:j_id271:j_id274")

            #detalhes = navegador.find_elements('xpath', '//*[@id="consultaProcessoTerceirosList:0:j_id271:j_id274"]/img')

            # Processo não encontrado
            #if len(detalhes) == 0:
               # naoencontrados.append(processo)
              #  print("Primeiro site: processo não encontrado.")
             #   continue

            #navegador.find_element('xpath', '//*[@id="consultaProcessoTerceirosList:0:j_id271:j_id274"]/img').click()

            #navegador.find_element('xpath', '//*[@id="modal:motivacaoDecoration:motivacao"]').send_keys("consulta processual")

            #navegador.find_element('xpath', '//*[@id="modal:btnGravar"]').click()

            #navegador.close()

            #navegador.find_element('id', "pesquisarProcessoTerceiroForm:nrProcessoDecoration:nrProcesso").clear()


    # Segundo site
    def segundosite(self):

        # Entrar
        navegador.get('https://pje.jfpb.jus.br/pje/Processo/ConsultaProcesso/listView.seam')

        navegador.find_element('id', "validadeCertificadoModalhidelink").click()

        # Pesquisar
        for nencontrei in naoencontrados:

            print("Entrou no for segundo site.")
            navegador.find_element('id', "consultarProcessoForm:numeroProcessoDecoration:numeroProcesso").send_keys(nencontrei)

            navegador.find_element('id', "consultarProcessoForm:searchButton").click()

            wait_load(navegador)

            detalhes = navegador.find_elements('id', "consultaProcessoTerceirosList:0:j_id271:j_id274")

            # Processo não encontrado
            if len(detalhes) == 0:

                for proc in processos:
                    "Nenhum processo encontrado."

            # Detalhes
            navegador.find_element('xpath', '//*[@id="idLegenda1"]/table/tbody/tr[3]/td[1]/img').click()

            navegador.find_element('id', "modal:motivacaoDecoration:motivacao").send_keys("consulta processual")

            navegador.find_elements('id', "consultaProcessoTerceirosList:0:j_id271:j_id274").click()

            navegador.find_element('id', "modal:motivacaoDecoration:motivacao").send_keys("consulta processual")

            navegador.find_element('id', "modal:btnGravar").click()

            navegador.close()

            navegador.find_element('id', "pesquisarProcessoTerceiroForm:nrProcessoDecoration:nrProcesso").clear()


# Abrir navegador
navegador = webdriver.Chrome()

naoencontrados = []

processos = ("08078097420174058200", "08090663720174058200", "08997543520204058201", "08007543520184058201")

busca = Processo()
busca.primeirosite()
busca.segundosite()
