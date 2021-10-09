import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("version"+str(sqlite3.version))
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def add_item(conn, item):

    sql = ''' INSERT INTO eletronics(id,row,colum,name,buy_date,n,link,description)
              VALUES(?,?,?,?,?,?,?,?)
              '''
    cur = conn.cursor()
    cur.execute(sql, item)
    conn.commit()


def select_item_by_name(conn, name):
    """
    Query tasks by name
    :param conn: the Connection object
    :param name:
    :return: row
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM eletronics WHERE name=? ",
                (name,))  # need to be tuple

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_all_items(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return: row
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM eletronics")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def delete_item(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the item
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    # APAGA A PORRA TODA
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
