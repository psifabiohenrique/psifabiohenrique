import kivy
from kivy.app import App
from kivy.lang import Builder
kivy.require('2.0.0')


code = """

BoxLayout:
    Button:
        text: '1'
    Button:
        text: '2'

"""


class Estudo1App(App):
    def build(self):
        return Builder.load_string(code)


janela = Estudo1App()
janela.run()
