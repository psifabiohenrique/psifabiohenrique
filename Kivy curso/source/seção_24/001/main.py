import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
kivy.require('2.0.0')


class Tela1(BoxLayout):  # classe da primeira janela do programa
    def on_press_bt(self):  # função para mudar as janelas do programa
        janela.root_window.remove_widget(janela.root)   # remove a janela anterior
        janela.root_window.add_widget(Tela2())  # adiciona a nova janela

    def __init__(self, **kwargs):   # inicia uma nova instância sempre que Tela1 for invocada
        super(Tela1, self).__init__(**kwargs)
        self.orientation = 'vertical'   # determina que os widgets sejam empilhados na vertical
        bt1 = Button(text='Clique')     # adiciona um botão
        bt1.on_press = self.on_press_bt     # determina que, quando o botão for pressionado, a função seja invocada
        self.add_widget(bt1)    # adiciona o botão ao widget
        self.add_widget(Button(text='bt2'))  # repete as duas linhas de cima em uma
        self.add_widget(Button(text='bt3'))


class Tela2(BoxLayout):
    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela1())

    def __init__(self, **kwargs):
        super(Tela2, self).__init__(**kwargs)
        self.orientation = 'vertical'
        bt = Button(text='Clique')
        bt.on_press = self.on_press_bt
        self.add_widget(bt)


class KVvsPY(App):  # cria uma instância de App
    def build(self):
        return Tela1()  # retorna a essa instância a tela1


janela = KVvsPY()
janela.run()
