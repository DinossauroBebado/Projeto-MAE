import sqlite3
from sqlite3 import Error
import random


def generate_id():
    return random.randint(10, 30)


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("version"+str(sqlite3.version))
    except Error as e:
        print(e)
    return conn


def create_table(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    sql_create_eletronics_table = """ CREATE TABLE IF NOT EXISTS eletronics (
                                        id integer PRIMARY KEY,
                                        row integer NOT NULL,
                                        colum integer NOT NULL,
                                        name text NOT NULL,
                                        type text,
                                        buy_date_day integer,
                                        buy_date_month integer,
                                        buy_date_year integer,
                                        n integer,
                                        link text,
                                        description text
                                    ); """
    try:
        c = conn.cursor()
        c.execute(sql_create_eletronics_table)
    except Error as e:
        print(e)


def add_item(conn, item):

    sql = ''' INSERT INTO eletronics(id,row,colum,name,type,buy_date_day,buy_date_month,buy_date_year,n,link,description)
              VALUES(?,?,?,?,?,?,?,?,?,?,?)
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

    return rows


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
