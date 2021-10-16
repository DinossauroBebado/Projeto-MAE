from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Inventario(BoxLayout):
    ...


class MainApp(App):
    def build(self):

        return Inventario()

    def pesquisa(self):
        text = self.root.ids.pesquisa.text
        print(text)


if __name__ == "__main__":

    MainApp().run()
