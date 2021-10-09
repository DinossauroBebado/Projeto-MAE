"""
Esse projeto é para ter o controle de um banco de dados com os componentes
eletronicos da DinoCaverna.

Eventualmente esse programa vai receber consultas de ESPs ou hhtp para acessar essas informações


"""

import DataBase


def main():
    conn = DataBase.create_connection(r"db\eletronicos.db")

    sql_create_eletronics_table = """ CREATE TABLE IF NOT EXISTS eletronics (
                                        id integer PRIMARY KEY,
                                        row integer NOT NULL,
                                        colum integer NOT NULL,
                                        name text NOT NULL,
                                        buy_date text,
                                        n integer,
                                        link text,
                                        description text
                                    ); """

    # create tables
    if conn is not None:
        # create projects table
        DataBase.create_table(conn, sql_create_eletronics_table)

    else:
        print("Error! cannot create the database connection.")

    with conn:
        item = (0, 0, 0, "Led Branco", '2021-10-08', 25,
                'link', "Led branco com diversos tamanhos")

        """add_item(conn,item )"""

        DataBase.select_task_by_priority(conn, 0)

        print("2. Query all tasks")
        DataBase.select_all_items(conn)


if __name__ == "__main__":

    main()
