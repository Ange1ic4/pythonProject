import pyautogui
import time

pyautogui.PAUSE = 0.5

# abrir o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)

# escolher o perfil do google
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')

# digitar o site
pyautogui.write("https://webmail-seguro.com.br/bauheradvogados.adv.br/")
pyautogui.press('enter')

# encontrar o campo "email" e preencher
time.sleep(1)
pyautogui.write('giovanna@bauheradvogados.adv.br')
pyautogui.press('tab')
pyautogui.write('TempP@ss123')
pyautogui.press('enter')

#encontrar o campo "senha" e preencher
pyautogui.press('tab')
pyautogui.write('TempP@ss123')
pyautogui.press('enter')

def mover_email(tipo, id):
    seta = navegador.find_elements(tipo, id)
    while len(seta) != 0:
        seta = navegador.find_elements(tipo, id)