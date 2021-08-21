from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


ed = ''


def click():
    print(ed.text)


def build():
    layout = FloatLayout()
    global ed
    ed = TextInput(text='Seu texto aqui!')
    ed.size_hint = None, None
    ed.height = 300
    ed.width = 400
    ed.x = 60
    ed.y = 250

    bt = Button(text='Clique aqui!')
    bt.size_hint = None, None
    bt.width = 200
    bt.height = 50
    bt.y = 150
    bt.x = 170

    bt.on_press = click

    layout.add_widget(ed)
    layout.add_widget(bt)

    return layout


janela = App()
janela.title = 'Primeiro App'
Window.size = 600, 600
janela.build = build
janela.run()
