
import pyautogui as pag
import pyperclip as ppp
import time

var = ['llllssss', 'lllssssl', 'llssssll', 'lsssslll', 'sllllsss', 'ssllllss', 'ssslllls', 'ssssllll', 'lslslsls', 'slslslsl', 'ssllssll','lllslsss','lllsslss','lllsssls','llssllss','llsllsss']
rep = 'lslslsls'

pag.PAUSE = 5

def playvar():
    global var
    for c in range(5):
        pag.write(var[0], interval= .3)
        tranf = var[0]
        var.pop(0)
        var.append(tranf)

def playrep():
    for c in range(5):
        pag.write(rep, interval= .3)

def cond():
    for c in range(6):
        playvar()
        playrep()

def condcom():
    for c in range(6):
        pag.PAUSE = 1
        pag.write('slsslsll', interval= .3)
        time.sleep(3)
        pag.click(x=2753, y=491, clicks= 2)
        pag.write('slsslsll', interval= .3)
        time.sleep(3)
        pag.click(x=2753, y=491, clicks= 2)



pag.hotkey('alt', 'tab')
pag.click(x=2405, y=455)
pag.write(' ')

cond()
time.sleep(182)
pag.write(' ')
condcom()
time.sleep(182)
pag.write(' ')
cond()

