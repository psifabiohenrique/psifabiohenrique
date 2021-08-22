import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
kivy.require('2.0.0')


class MinhaTela(BoxLayout):
    def click(self):
        print('oi')
        self.ids.lb1.text = ''
        self.ids.lb2.text = '10'


class Estudo4App(App):
    pass


janela = Estudo4App()
janela.run()
