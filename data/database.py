import sqlite3

def connect(con, cursor):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    return con, cursor

def disconnect(con):
    con.commit()
    con.close()