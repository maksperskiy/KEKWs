from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers.html import HtmlLexer
from kivy.config import Config


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):



        f1 = FloatLayout(size = (300, 300))

        f1.add_widget(Button(text="Hello World!",
                      font_size = 30,
                      on_press = self.btn_press,
                      background_color = [1, 0, 0, 1],
                      background_normal = '',
                      size_hint = (.5, .25),
                      pos = (0, 0)))

        return f1
    def btn_press(self, instance):
        print('ДОРОу')
        instance.text = 'кукусики'

if __name__ == "__main__":
    MyApp().run()