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
        loading = navegador.find_elements('class name', 'loading')
        if len(loading) > 0:
            try:
                loading[0].is_displayed()
            except:
                pass

            continue

        break


navegador = webdriver.Chrome()

# Entrar no site
navegador.get('https://cpe.web.stj.jus.br/#/')

processos = ("00008437020158210133", "10036986220208260077",  "81681311220228050001", "10858905120188260100")

for processo in processos:

    goback = navegador.find_elements('xpath', "/html/body/a")
    if len(goback) != 0:
        navegador.close()

        navegador = webdriver.Chrome()

        # Entrar no site
        navegador.get('https://processo.stj.jus.br/processo/pesquisa/?aplicacao=processos.ea')

    aguarda_elemento('id', "idBotaoPesquisarFormularioExtendido")

    # Preencher o número do processo
    navegador.find_element('id', "idNumeroUnico").send_keys(processo)

    # Clicar em pesquisar
    navegador.find_element('id', "idBotaoPesquisarFormularioExtendido").click()

    nprocesso = navegador.find_elements('id', "idSpanAbaDetalhes")

    if len(nprocesso) == 0:
        navegador.find_element('id', "idBotaoFormularioExtendidoNovaConsulta").click()
        print("NENHUM PROCESSO ENCONTRADO.")
        continue

    # Encontrar o Recorrente
    titulos = navegador.find_elements('class name', "classSpanDetalhesLabel")

    conteudos = navegador.find_elements('class name', "classSpanDetalhesTexto")

    for titulo, conteudo in zip(titulos, conteudos):
        a = titulo.text
        b = conteudo.text
        if (a == "RECORRENTE:"):
            print(a, b)
        if (a == "RECORRIDO :"):
            print(a, b)
        if (a == "ADVOGADO:"):
            print(a, b)
        if (a == "AUTUAÇÃO:"):
            print(a, b)


    navegador.find_element('id', "idSpanAbaFases").click()

    fase = navegador.find_elements('class name', "classDivFaseLinha")

    for etapa in fase:
        print(etapa.text)

    navegador.find_element('id', "idBotaoFormularioExtendidoNovaConsulta").click()


print()
time.sleep(5)
