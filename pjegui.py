from datetime import datetime, date
from selenium import webdriver
from selenium.common import ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import time


class Processo:

    def __init__(self):
        self.navegador = webdriver.Chrome()
        self.naoencontrados = []

    def primeirosite(self):

        # Entrar no site
        self.navegador.get('https://pje.jfpb.jus.br/pje/login.seam')

        self.aguarda_elemento('id', 'btnUtilizarApplet')

        self.navegador.execute_script('document.getElementById("btnUtilizarApplet").click()')

        while True:
            try:
                self.navegador.find_element('id', "loginAplicacaoButton").click()
            except:
                fechar = self.navegador.find_elements('xpath', '//*[@id="panelAmbienteContentTable"]/tbody/tr[2]/td/table/tbody/tr[7]/td[2]/input[3]')
                if len(fechar) > 0:
                    if fechar[0].is_displayed():
                        self.navegador.find_element('xpath', '//*[@id="panelAmbienteContentTable"]/tbody/tr[2]/td/table/tbody/tr[7]/td[2]/input[3]').click()

                        continue

                break

        self.aguarda_elemento('xpath', '//*[@id="validadeCertificadoModalhidelink"]')

    def segundosite(self):
        processos = ("08078097420174058200", "08090663720174058200", "08997543520204058201", "08007543520184058201", "00001376720235130008", "00000493820235130005", "08345348520228152001", "08063404120238152001", "00021824920224058200")
        self.navegador.get('https://pje.jfpb.jus.br/pje/Processo/ConsultaProcessoTerceiros/listView.seam')

        self.wait_invertido('xpath', '//*[@id="validadeCertificadoModalhidelink"]')

        for processo in processos:
            formulario = self.navegador.find_element('xpath', '//*[@id="pesquisarProcessoTerceiroForm:nrProcessoDecoration:nrProcesso"]')
            formulario.send_keys(Keys.CONTROL, 'a')
            formulario.send_keys(processo)

            self.botao_pesquisar('id', "pesquisarProcessoTerceiroForm:searchButton")

            self.wait_load('xpath', '//*[@id="modalStatusContentTable"]/tbody/tr/td')

            detalhes = self.navegador.find_elements('xpath', '//*[@id="consultaProcessoTerceirosList:0:j_id271:j_id274"]/img')

            if len(detalhes) == 0:
                self.naoencontrados.append(processo)
                continue

            self.wait_to_be_interectable('xpath', '//*[@id="consultaProcessoTerceirosList:0:j_id271:j_id274"]/img')

            self.navegador.find_element('xpath', '//*[@id="consultaProcessoTerceirosList:0:j_id271:j_id274"]/img').click()

            self.navegador.execute_script('document.getElementById("modal:motivacaoDecoration:motivacao").innerHTML = "Consulta processual"; ')

            self.navegador.execute_script('document.getElementById("modal:btnGravar").click();')

            self.wait_load('xpath', '//*[@id="modalStatusContentTable"]/tbody/tr/td')

            # Acessar a aba "Detalhes" e fechar
            self.navegador.switch_to.window(self.navegador.window_handles[1])
            self.aguarda_elemento('id', 'j_id845:j_id846')
            self.navegador.close()
            self.navegador.switch_to.window(self.navegador.window_handles[0])

        print(self.naoencontrados)

    def terceirosite(self):

        self.navegador.get('https://pje.jfpb.jus.br/pje/Processo/ConsultaProcesso/listView.seam')

        self.wait_invertido('xpath', '//*[@id="validadeCertificadoModalhidelink"]')

        for naoencontrado in self.naoencontrados:
            formulario = self.navegador.find_element('xpath', '//*[@id="consultarProcessoForm:numeroProcessoDecoration:numeroProcesso"]')
            formulario.send_keys(Keys.CONTROL, 'a')
            formulario.send_keys(naoencontrado)

            self.botao_pesquisar('xpath', '//*[@id="consultarProcessoForm:searchButton"]')

            self.wait_load('xpath', '//*[@id="modalStatusContentTable"]/tbody/tr/td')

            detalhes = self.navegador.find_elements('xpath', '//*[@id="idLegenda1"]/table/tbody/tr[3]/td[1]')

            # Caso não ache nenhum processo, este não é armazenado
            if len(detalhes) == 0:
                continue

            # ADAPTAR A PARTIR DAQUI
            # Detalhes
            self.navegador.execute_script('document.getElementById("").click();')

            self.navegador.execute_script('document.getElementById("").innerHTML = "Consulta processual"; ')

            self.navegador.execute_script('document.getElementById("").click();')

            # Carregamento da página "Detalhes"
            self.wait_load('xpath', '')

            # Acessar "Detalhes" e fechar aba
            self.navegador.switch_to.window(self.navegador.window_handles[1])
            self.aguarda_elemento('id', '')
            self.navegador.close()
            self.navegador.switch_to.window(self.navegador.window_handles[0])


    def aguarda_elemento(self, tipo, id):
        botao = self.navegador.find_elements(tipo, id)
        while len(botao) == 0:
            botao = self.navegador.find_elements(tipo, id)

    def wait_load(self, tipo, id):
        while True:
            loading = self.navegador.find_elements(tipo, id)
            if loading[0].is_displayed():
                continue
            break

    def wait_invertido(self, tipo, id):
        while True:
            loading = self.navegador.find_elements(tipo, id)
            if loading[0].is_displayed():
                try:
                    self.navegador.find_element(tipo, id).click()
                except:
                    pass
                continue
            break

    def botao_pesquisar(self, tipo, id):
        while True:
            try:
                self.navegador.find_element(tipo, id).click()
                break
            except:
                continue

    def wait_to_be_interectable(self, tipo, id):
        while True:
            try:
                element = self.navegador.find_elements(tipo, id)
                element[0].click()
                break
            except ElementNotInteractableException:
                pass
            except StaleElementReferenceException:
                pass

p = Processo()
p.primeirosite()
p.segundosite()
p.terceirosite()
