from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.graphics import (Color, Line, Rectangle, Ellipse)
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.config import Config


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '640')

class MainWidget(Label):
    Label.text = 'xaxaxaxa'
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 0, 1, 1)
            rad = 30
            Ellipse(pos = (touch.x - rad/2, touch.y - rad/2), size = (rad, rad))
            touch.ud['line'] = Line(points = (touch.x, touch.y), width = 15)

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)


class BoxApp(App):
    def build(self):
        application = BoxLayout()
        self.painter = MainWidget()
        application.add_widget(self.painter)


        main_box = Label()
        text_box = Label()


        return application

if __name__ == "__main__":
    BoxApp().run()