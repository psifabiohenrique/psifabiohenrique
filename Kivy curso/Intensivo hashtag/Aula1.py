# Primeiro passo entrar no Mapa Bonus
# Segundo passo começar os ataques
# Terceiro passo verificar se já finalizamos o mapa bonus
# Quarto passo, se finalizou o mapa bonus então iniciar de novo
# Se não, continuar os ataques

import pyautogui as pag
import pyperclip as ppp
import time
import pandas as pd


#PyAutoGui não digita caracteres especiais, para isso usamos o PyPerClip

link = 'www.psifabiohenrique.tk'   # Cria variável com texto usando caractere especial

ppp.copy(link) # digita o que estiver entre parênteses, não precisa estar em variável, posso passar um string direto

pag.PAUSE = 1 # Espera 1 segundo entre cada ação do PyAutoGui // funciona para todos os comandos do PyAutoGui
pag.press('win')
pag.hotkey('Crtl','c')
pag.write('Escreva isso')
time.sleep(5) # Espera 5 segundos antes do próximo comando
pag.click(x= 100, y= 100, clicks=2, button= 'right')
pag.position() # Detecta a posição do mouse

