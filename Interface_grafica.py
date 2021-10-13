from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Inventario(BoxLayout):
    ...


class MainApp(App):
    def build(self):

        return Inventario()


MainApp().run()
