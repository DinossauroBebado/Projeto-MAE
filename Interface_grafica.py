

import DataBase
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty

infos = ["id", 'x', 'y', 'name', 'type',
         'buy_date_day', 'buy_date_month', 'buy_date_year',
         "unity", 'link', 'description']

botoes = []

conn = DataBase.create_connection(r"db\eletronicos.db")


class Inventario(BoxLayout):
    ...


class MainApp(App):

    def build(self):

        return Inventario()

    def check_db(self, item) -> infos:
        db = DataBase.select_item_by_name(conn, str(item))
        db = db[0]
        db_infos = {infos[i]: db[i] for i in range(len(infos))}
        return db_infos

    def box_color(self, id):
        # parse db to dict pos :low
        # check if id match pos
        # change color
        ...

    def box_hover(self):
        # when mouse hover over button update indo displayed
        ...

    def teste(self):
        self.change_color("0_0")

    def teste_one(self):
        self.change_color("4_7")

    def reset_color(self):
        """
        Essa função tira a cor mudada pela pesquisa
        ela faz isso salvando os botoes que foram pesquisados e 
        tira a cor do ultimo botao na lista
        """
        ident = botoes[-1]

        self.root.ids[ident].background_color = [1, 1, 1, 1]

    def change_color(self, ident):
        """
        Essa função muda a cor do botao com o item pesquisado


        """
        if len(botoes) > 0:
            self.reset_color()

        self.root.ids[ident].background_color = [0, 1.3, 2, 1]
        botoes.append(ident)

    def pesquisa(self):
        text = self.root.ids.pesquisa.text
        self.root.ids.pesquisa.text = ""
        self.update_info(text)

    def update_info(self, text):

        db_infos = self.check_db(text)

        pos = f"{db_infos['x']}_{db_infos['y']}"
        self.change_color(pos)
        self.root.ids.name.text = db_infos['name']
        self.root.ids.unity.text = str(db_infos['unity'])
        self.root.ids.pos.text = str(str(db_infos['x'])+","+str(db_infos['y']))
        self.root.ids.type.text = db_infos['type']
        self.root.ids.buy_date.text = f"{db_infos['buy_date_day']}/{db_infos['buy_date_month']}/{db_infos['buy_date_year']}"
        self.root.ids.link.text = str(db_infos['link'])
        self.root.ids.description.text = db_infos['description']

    def add(self):
        """
        Adiciona infomações ao banco de dados
        item = (0, 0, 0, "Led Branco","led",8,12,34, 25,
                'link', "Led branco com diversos tamanhos")
        """

        index = self.root.ids.pos.text.index(",")
        x = self.root.ids.pos.text[:index]
        y = self.root.ids.pos.text[index+1:]

        day = int(self.root.ids.buy_date.text[:2])
        month = int(self.root.ids.buy_date.text[3:5])
        year = int(self.root.ids.buy_date.text[6:])
        item = (
            DataBase.generate_id(),
            int(x),  # x
            int(y),  # y
            self.root.ids.name.text,
            self.root.ids.type.text,
            day,
            month,
            year,
            int(self.root.ids.unity.text),
            self.root.ids.link.text,
            self.root.ids.description.text
        )

        DataBase.add_item(conn, item)

        self.root.ids.pos.text = ""  # x
        self.root.ids.pos.text = ""  # y
        self.root.ids.name.text = ""
        self.root.ids.type.text = ""
        self.root.ids.buy_date.text = ""
        self.root.ids.unity.text = ""
        self.root.ids.link.text = ""
        self.root.ids.description.text = ""


if __name__ == "__main__":

    MainApp().run()
