import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
kivy.require('2.0.0')


def funcSelf(x):
    print('funcSelf')


Button.funcSelf = funcSelf


class MinhaTela(BoxLayout):
    def funcRoot(self):
        print('funcRoot')


class EstudoApp(App):
    def funcApp(self):
        print('funcApp')


janela = EstudoApp()
janela.run()
