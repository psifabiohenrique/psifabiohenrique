from re import S
import pyautogui as pag
import pyperclip as ppp
import time
import clipboard as cb

# link diário de bordo (https://int13.seafight.com/index.es?action=internalCabin&subact=Logbook)
checagem = False
inicio = ''
msg = ''
clickentermb = []
clickexecmb = []
clicksairmb = []
pag.PAUSE= 2

pos = int(input('1 para calibrar posições, 0 para seguir: '))

def sairmb():
    global msg
    global clicksairmb
    pag.hotkey('ctrl', 'shift', 'tab')
    pag.hotkey('f5')
    time.sleep(5)
    pag.click(x=clicksairmb[0], y=clicksairmb[1], interval=.3, clicks=3)
    pag.hotkey('ctrl', 'c')
    verificar = cb.paste()
    pag.hotkey('ctrl', 'tab')
    if verificar == msg:
        entermb()
    else:
        msg = verificar
        execmb()

def execmb():
    global clickexecmb
    for c in range(100):
        # pag.write('e')
        # pag.write('q')
        time.sleep(2)
        pag.click(x=clickexecmb[0], y=clickexecmb[1], clicks=2)
        print(c)
    pag.write('8')
    sairmb()

def entermb():
    global clickentermb
    pag.click(x=clickentermb[0], y=clickentermb[1])
    pag.write('4')
    time.sleep(17)
    execmb()

def posi():
    global clickentermb
    global clickexecmb
    global clicksairmb
    clickentermb = []
    for c in range (2):
        var = int(input(f'Valor {c} da janela do navegador: '))
        clickentermb.append(var)
    clickexecmb = []
    for c in range (2):
        var = int(input(f'Valor {c} da janela do navegador: '))
        clickexecmb.append(var)
    clicksairmb = []
    for c in range (2):
        var = int(input(f'Valor {c} da janela do navegador: '))
        clicksairmb.append(var)
    a = input('Digite qualquer tecla para iniciar o MB: ')
    entermb()


if pos == 1:
    for c in range(3):
        a = input(f'Digite qualquer tecla para verificar a posição {c}')
        time.sleep(5)
        print(pag.position())
elif pos == 0:
    posi()
else:
    exit()


# Entrar no MB



# Selecionar alvos e disparar


while checagem is False:
    inicio = input('Digite S para iniciar: ')

    if inicio == 'S' or inicio == 's':
        entermb()
        checagem = True

    else:
            checagem = False





# Parar e entrar novamente no MB
