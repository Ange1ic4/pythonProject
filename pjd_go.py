from datetime import datetime, date
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, StaleElementReferenceException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


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


class Gopjd:
    def __init__(self):
        pass

    driver = webdriver.Chrome()

    def entrar_no_site(self):
        # Abrir navegador

        self.driver.get('https://pjd.tjgo.jus.br/')

        self.driver.find_element_by_xpath('//*[@id="loginbox"]').send_keys('96586419115')
        self.driver.find_element_by_xpath('//*[@id="Senha"]').send_keys('Vieiralopes52@')
        self.driver.find_element_by_id('teclashiftN').click()

        self.aguarda_elemento('id', 'nomeUsuarioTopo')

    def busca_processo(self):
        num_processos = ('53168101420178090051', '54299684720178090051', '52973625520178090051', '54442750620178090051','54182530820178090051', '54411659620178090051', '54249933120178090164', '54195201520178090051', '54128560320178090007', '54099303320178090174', '52864292320178090051', '51426709820178090051', '54462636220178090051', '54407960520178090051')

        for num_processo in num_processos:
            self.wait_to_be_interectable('xpath', '//*[@id="btnBuscaProcessoMenuPrincipal"]/i')
            self.aguarda_elemento('xpath', '//*[@id="ProcessoNumero"]')
            campo_pesquisa = self.driver.find_element_by_xpath('//*[@id="ProcessoNumero"]')
            numero_busca = num_processo[:9]
            campo_pesquisa.send_keys(numero_busca)
            situacao = self.driver.find_elements_by_class_name('select2-selection__clear')
            situacao[0].click()
            self.driver.find_element_by_xpath('//*[@id="divFiltros"]/label').click()

            # self.driver.execute_script("situacao = document.getElementsByClassName('select2-selection__rendered'); situacao[0].innerText == ' ';")


            self.wait_to_be_interectable('xpath', '//*[@id="btnConsultar"]')
            self.wait_load()

            numero_processo = self.driver.find_elements_by_xpath('//*[@id="tituloCapaProcesso"]')

            if len(numero_processo) == 0:
                print("Nenhum registro encontrado.")
                self.driver.find_element_by_xpath('//*[@id="limpar"]')
                self.wait_load()
                continue

            self.wait_load()

            # Número do processo
            numero = numero_processo[0].text.split(' ')
            print("Número do processo: " + numero[1])
            # Até aqui OK

            self.wait_to_be_interectable('xpath', '//*[@id="listaMenuOpcoesProcesso"]/li[7]/a')
            self.wait_load()

            tabela_1 = self.driver.find_elements_by_xpath('//*[@id="tabListaAdvogadoParte"]/tr[1]/td')
            tabela_2 = self.driver.find_elements_by_xpath('//*[@id="tabListaAdvogadoParte"]/tr[2]/td')

            for n in range(4):
                if n == 0:
                    print("Partes:")
                    print(tabela_1[n].text)
                    print(tabela_2[n].text)
                if n == 2:
                    print("Advogados:")
                    print(tabela_1[n].text)
                    print(tabela_2[n].text)

            self.wait_to_be_interectable('xpath', '//*[@id="menuOpcoesProcessoMovimentacoes"]/a')
            self.wait_load()
            fases = self.driver.find_elements_by_xpath('/html/body/div[1]/div[5]/section/div/div[2]/div/div[3]/div[2]/div/div[3]/div/table/tbody/tr')
            print(len(fases))
            for fase in fases:
                print(fase.text)

            # self.home_button()

            # self.wait_to_be_interectable('xpath', '/html/body/div[1]/header/nav/div[1]/button')
            # self.wait_to_be_interectable('xpath', '//*[@id="linkPaginaInicial"]/i')

            # if coluna == "Nome da Parte":
                #     print(tabela_1.text)
                #     print(tabela_2.text)
                # if coluna == "Nome do Advogado":
                #     print(tabela_1.text)
                #     print(tabela_2.text)

    def aguarda_elemento(self, tipo, id):
        botao = self.driver.find_elements(tipo, id)
        while len(botao) == 0:
            botao = self.driver.find_elements(tipo, id)

    def wait_to_be_interectable(self, tipo, id):
        while True:
            try:
                element = self.driver.find_elements(tipo, id)
                element[0].click()
                break
            except ElementNotInteractableException:
                pass
            except StaleElementReferenceException:
                pass
            except ElementClickInterceptedException:
                pass

    def wait_load(self):
        while True:
            loading = self.driver.find_elements_by_xpath('/html/body/div[3]/span/i')
            if len(loading) > 0:
                try:
                    loading[0].is_displayed()
                except:
                    pass

                continue

            break

    def home_button(self):
        while True:
            home = self.driver.find_elements_by_xpath('//*[@id="linkPaginaInicial"]')
            if len(home) > 0:
                try:
                    home[0].is_displayed()
                    home[0].click()
                    break
                except:
                    self.driver.find_element_by_xpath('/html/body/div[1]/header/nav/div[1]/button/i').click()
                    pass

                continue

            break


busca = Gopjd()

busca.entrar_no_site()
busca.busca_processo()
