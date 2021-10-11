from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(MDApp):
    def build(self):
        box1 = BoxLayout(orientation='vertical')
        box2 = BoxLayout(orientation='horizontal')

        projeto = MDLabel(text="PROJETO MAE", halign="left")
        projeto.font_size = 50

        box3 = BoxLayout(orientation='vertical')
        nome = MDLabel(text="Nome", halign="left")
        pos = MDLabel(text="Posição", halign="left")
        tipo = MDLabel(text="Tipo", halign="left")
        N = MDLabel(text="N", halign="left")
        data_compra = MDLabel(text="Data compra", halign="left")
        link = MDLabel(text="Link", halign="left")
        descricao = MDLabel(text="Discrição", halign="left")

        pesquisar = TextInput()
        pesquisar.text = "Pesquisar "
        box3.add_widget(pesquisar)
        box3.add_widget(nome)
        box3.add_widget(tipo)
        box3.add_widget(pos)
        box3.add_widget(N)
        box3.add_widget(data_compra)
        box3.add_widget(link)
        box3.add_widget(descricao)

        btn = Button(
            text='Caixas',

        )
        btn.font_size = 50

        box2.add_widget(box3)
        box2.add_widget(btn)

        box1.add_widget(projeto)

        box1.add_widget(box2)

        return box1
