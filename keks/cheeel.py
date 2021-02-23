from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '800')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

from random import random
from kivy.core.window import Window
from kivy.graphics import (Color, Ellipse, Rectangle, Line)


class Container(BoxLayout):
    pass




class MainLabel(Label):



    # words = ['kek', 'sila', 'lul\'nya', '4eburek']
    textatilio = open('text.txt', 'rt')
    txtfile = ''
    for line in textatilio:
        txtfile += line
    words = txtfile.split()
    i = 0

    speed = 0.1

    prev_touch_x = 0
    prev_touch_y = 0
    play = True
    font_size = 26
    def on_touch_down(self, touch):

        #state
        self.play = not self.play

        # lil
        with self.canvas:
            Color(random(), random(), random(), 1)
            rad = 10
            Ellipse(pos=(touch.x - rad / 2, touch.y - rad / 2), size=(rad, rad))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=5)
        # keks
        self.prev_touch_x = touch.x
        self.prev_touch_y = touch.y

    def on_touch_move(self, touch):
        self.play = False
        touch.ud['line'].points += (touch.x, touch.y)
        if touch.x > self.prev_touch_x + 50 and self.i > 0:
            self.i -= 1
            self.prev_touch_x = touch.x
        elif touch.x < self.prev_touch_x - 50 and self.i < len(self.words) - 1:
            self.i += 1
            self.prev_touch_x = touch.x
        if touch.y > self.prev_touch_y + 50 and self.speed >= 0.2:
            self.speed -= 0.1
            self.play = True
            print(self.speed)
            self.prev_touch_y = touch.y
        elif touch.y < self.prev_touch_y - 50 and self.speed <= 0.9:
            self.speed += 0.1
            self.play = True
            print(self.speed)
            self.prev_touch_y = touch.y




    def update(self, *args):
        self.text = self.words[self.i]
        if self.play and self.i < len(self.words) - 1:
            self.i += 1
            self.color = (1, 1, 1, 1)


    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0, 0, 1)
            Rectangle(pos=self.pos, size=self.size)


class ReadApp(App):
    def build(self):


        main_label = MainLabel()



        #Как изменить скорость?


        Clock.schedule_interval(main_label.update, main_label.speed)


        return main_label


if __name__ == '__main__':
    ReadApp().run()