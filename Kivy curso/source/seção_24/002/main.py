import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
kivy.require('2.0.0')


class Tela1(BoxLayout):  # classe da primeira janela do programa
    def on_press_bt(self):  # função para mudar as janelas do programa
        janela.root_window.remove_widget(janela.root)   # remove a janela anterior
        janela.root_window.add_widget(Tela2())  # adiciona a nova janela


class Tela2(BoxLayout):
    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela1())


class KVvsPY2(App):  # cria uma instância de App
    def build(self):
        return Tela1()  # retorna a essa instância a tela1


janela = KVvsPY2()
janela.run()
