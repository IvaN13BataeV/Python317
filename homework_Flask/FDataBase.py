import time
import sqlite3
import math
import re
from flask import url_for


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def add_news(self, title, text, url):
        try:
            self.__cur.execute("SELECT COUNT() as `count` FROM news WHERE url LIKE ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Новость с таким url уже существует")
                return False
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO news VALUES (NULL, ?, ?, ?, ?)", (title, text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления новости в БД " + str(e))
            return False
        return True

    def get_news(self, alias):
        try:
            self.__cur.execute(f"SELECT title, text FROM news WHERE url='{alias}'")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения новости из БД " + str(e))

        return False, False

    def get_news_annonce(self):
        try:
            self.__cur.execute("SELECT id, title, text, url FROM news ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения новостей из БД " + str(e))

        return []
