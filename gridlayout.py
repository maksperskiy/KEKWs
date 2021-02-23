from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.gridlayout import GridLayout


class BoxApp(App):
    def build(self):
        bl = GridLayout(cols=4, rows=5, padding=[30], spacing=30)

        for x in range(16):
            bl.add_widget(Button(text="lol"))

        return bl

if __name__ == "__main__":
    BoxApp().run()