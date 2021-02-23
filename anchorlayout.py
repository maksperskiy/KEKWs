from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class BoxApp(App):
    def build(self):
        bl = GridLayout(cols=4)


        bl.add_widget(Button(text="7"))
        bl.add_widget(Button(text="8"))
        bl.add_widget(Button(text="9"))
        bl.add_widget(Button(text="X"))

        bl.add_widget(Button(text="4"))
        bl.add_widget(Button(text="5"))
        bl.add_widget(Button(text="6"))
        bl.add_widget(Button(text="-"))

        bl.add_widget(Button(text="1"))
        bl.add_widget(Button(text="2"))
        bl.add_widget(Button(text="3"))
        bl.add_widget(Button(text="+"))

        bl.add_widget(Widget())
        bl.add_widget(Button(text="0"))
        bl.add_widget(Button(text="."))
        bl.add_widget(Button(text="="))

        return bl

if __name__ == "__main__":
    BoxApp().run()