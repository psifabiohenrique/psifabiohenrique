from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def build():
    layout = FloatLayout
    texto = TextInput(text='Digite algo')


janela = App()
janela.build = build
janela.run()
