from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout


class BoxApp(App):
    def build(self):
        bl = BoxLayout(orientation="horizontal",
                       padding=[50, 25],
                       spacing=100
                       )

        bl.add_widget(Button(text="lol"))
        bl.add_widget(Button(text="KEK"))
        bl.add_widget(Button(text="4eburek"))

        return bl

if __name__ == "__main__":
    BoxApp().run()