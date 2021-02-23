from kivy.uix.widget import Widget
from random import random
from kivy.core.window import Window
from kivy.graphics import (Color, Ellipse, Rectangle, Line)

class ScrollWidget(Widget):

    prev_touch_x = 0
    prev_touch_y = 0
    play = True
    def on_touch_down(self, touch):

        self.play = not self.play
        print(self.play)
        #lil
        with self.canvas:
            Color(random(), random(), random(), 1)
            rad = 10
            Ellipse(pos = (touch.x - rad/2, touch.y - rad/2), size = (rad, rad))
            touch.ud['line'] = Line(points = (touch.x, touch.y), width = 5)
        #keks
        self.prev_touch_x = touch.x
        self.prev_touch_y = touch.y


    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)
        if touch.x < self.prev_touch_x - 75:
            print('back')
            self.prev_touch_x = touch.x


    def on_touch_up(self, touch):
        if touch.x > self.prev_touch_x + 200:
            print('next')
        elif touch.x < self.prev_touch_x - 200:
            print('back')


        print('---------------------------------------')