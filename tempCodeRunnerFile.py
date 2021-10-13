
    conn = DataBase.create_connection(r"db\eletronicos.db")

    Interface_grafica.MainApp().run()

    """ # create tables
    if conn is not None:
        # create projects table
        DataBase.create_table(conn)

    else: