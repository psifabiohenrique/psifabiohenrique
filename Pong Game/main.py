from kivy.app import App
from kivy.uix.widget import Widget
import kivy.properties as prop
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector


class PongBall(Widget):
    # velocidade da bola nos eixos X e Y
    velocity_x = prop.NumericProperty(0)
    velocity_y = prop.NumericProperty(0)

    # a propriedade ReferenceListProperty é para nós usarmos uma
    # referência curta
    velocity = prop.ReferenceListProperty(velocity_x, velocity_y)

    # a função move vai mover a bola em passos
    # isso será chamado em intervalos iguais para animar a bola
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = prop.ObjectProperty(None)

    def update(self, dt):
        self.ball.move()
        if(self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1


class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return PongGame()


if __name__ == '__main__':
    PongApp().run()
