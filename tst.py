from datetime import datetime, date
from selenium import webdriver
from selenium.common import ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time


class Processo:

    def __init__(self):
        self.navegador = webdriver.Chrome()
        self.naoencontrados = []
        self.processos = ["0100026-67.2018.5.01.0019", "0100133-12.2018.5.01.0343", "0100329-36.2018.5.01.0000", "0100329-37.2018.5.01.0066"]

    def entrar_tst_sem_captcha(self):
        # Entrar no site

        self.navegador.get('https://aplicacao3.tst.jus.br/visualizacaoAutos/Iniciar.pub?load=1')

        # Acessar consulta
        pesquisar = self.navegador.find_element('xpath', '//*[@id="menu"]/ul/li[2]/span/a')

        ActionChains(self.navegador).move_to_element(pesquisar).perform()

        self.navegador.find_element('xpath', '//*[@id="menu"]/ul/li[2]/ul/li/a').click()

        for processo in self.processos:

            partes = processo.split("-")

            partes_2 = partes[1].split(".")

            self.navegador.find_element('xpath', '//*[@id="consultaProcessoForm"]/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[1]/input').send_keys(partes[0])

            self.navegador.find_element('xpath', '//*[@id="consultaProcessoForm"]/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input').send_keys(partes_2[0])

            self.navegador.find_element('xpath', '//*[@id="consultaProcessoForm"]/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/input').send_keys(partes_2[1])

            self.navegador.find_element('xpath', '//*[@id="consultaProcessoForm"]/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[4]/input').send_keys(partes_2[2])

            self.navegador.find_element('xpath', '//*[@id="consultaProcessoForm"]/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[5]/input').send_keys(partes_2[3])

            self.navegador.find_element('xpath', '//*[@id="consultaProcessoForm"]/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[6]/input').send_keys(partes_2[4])

            self.navegador.find_element('xpath', '//*[@id="botaoConsultar"]').click()

            consultar = self.navegador.find_elements('xpath', '//*[@id="botaoConsultar"]')

            # Consultar (quando o resultado devolve um resultado

            consultar_ok = self.navegador.find_elements('xpath', '//*[@id="resultadoProcessos"]/tbody/tr/td[3]/a')

            if len(consultar_ok) == 0:
                self.navegador.find_element('xpath', '//*[@id="botaoLimpar"]').click()
                print("Nenhum processo \n")

                continue

            #nprocesso = self.navegador.find_elements('xpath', '/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[2]/td/form/center/font/b')

            if len(consultar) > 0:
                # Consultar
                self.navegador.find_element('xpath', '//*[@id="resultadoProcessos"]/tbody/tr/td[3]/a').click()

                self.navegador.switch_to.window(self.navegador.window_handles[1])

                self.aguarda_elemento('class name', 'historicoProcesso')

                linhas = self.navegador.find_elements('class name', 'dadosProcesso')

                hisprocesso = self.navegador.find_elements('class name', 'historicoProcesso')

                for linha in linhas:
                    print(linha.text)

                print("Histórico do processo:")

                for h in hisprocesso:
                    print(h.text)

                print("Fim\n")
                self.navegador.close()

                self.navegador.switch_to.window(self.navegador.window_handles[0])

                self.navegador.find_element('xpath', '//*[@id="botaoLimpar"]').click()

                continue


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
p.entrar_tst_sem_captcha()