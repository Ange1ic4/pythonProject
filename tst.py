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
        self.processos = ("01000266720185010019", "01001331220185010343", "01003293620185010000", "01003293720185010066")

    def entrar_tst(self):
        self.navegador.get('http://aplicacao4.tst.jus.br/consultaProcessual/consultaTstNumUnica.do')

        for processo in self.processos:
            self.navegador.find_element('xpath', '//*[@id="consultaTstNumUnica:numeroTst"]').send_keys(processo)

            #Consultar
            self.navegador.find_element('xpath', '/html/body/table/tbody/tr[3]/td/table/tbody/tr[3]/td/form/table/tbody/tr[2]/td[2]/input[2]').click()

            #RECAPCHA (pode ter)

            self.carrega_pagina('class name', 'historicoProcesso', 'xpath', '/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[2]/td/form/center/font/b')

            nprocesso = self.navegador.find_elements('xpath', '/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[2]/td/form/center/font/b')

            if len(nprocesso) > 0:
                # Retornar à pesquisa
                self.navegador.find_element('xpath', '/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody/tr/td/a[1]/img').click()

                #RECAPTCHA (pode ter)
                self.aguarda_elemento('xpath', '//*[@id="consultaTstNumUnica:numeroTst"]') # Aguarda aparecer "Numero do processo"

                #Limpar pesquisa para não repetir o mesmo Processo
                self.navegador.find_element('xpath', '/html/body/table/tbody/tr[3]/td/table/tbody/tr[3]/td/form/table/tbody/tr[2]/td[2]/input[3]').click()
                continue

            linhas = self.navegador.find_elements('class name', 'dadosProcesso')

            hisprocesso = self.navegador.find_elements('class name', 'historicoProcesso')

            for linha in linhas:
                print(linha.text)

            print("Histórico do processo:")

            for h in hisprocesso:
                print(h.text)

            #Voltar para pesquisa
            self.navegador.find_element('xpath', '/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody/tr/td/a[1]/img').click()

            #RECAPTCHA

            self.aguarda_elemento('xpath', '//*[@id="consultaTstNumUnica:numeroTst"]')


    def aguarda_elemento(self, tipo, id):
        botao = self.navegador.find_elements(tipo, id)
        while len(botao) == 0:
            botao = self.navegador.find_elements(tipo, id)


    def wait_load(self, tipo, id):
        while True:
            loading = self.navegador.find_elements(tipo, id)
            if len(loading) > 0:
                try:
                    loading[0].is_displayed()
                except:
                    pass

                continue

            break


    def carrega_pagina(self, tipod, idd, tipon, idn):
        dados_do_processo = self.navegador.find_elements(tipod, idd)
        nprocesso = self.navegador.find_elements(tipon, idn)

        while True:
            if len(dados_do_processo) > 0:
                break

            if len(nprocesso) > 0 :
                break


p = Processo()
p.entrar_tst()