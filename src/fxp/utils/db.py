import sqlite3


def get_cursor(name):
    connect = sqlite3.connect(name)
    cursor = connect.cursor()
    return cursor

def create_table(cursor):
    sql = """
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            title TEXT(256) NOT NULL,
            "timestamp" REAL NOT NULL,
            "text" TEXT NOT NULL,
            img_link TEXT
        );
    """

def save_news(data, cursor):
    pass
