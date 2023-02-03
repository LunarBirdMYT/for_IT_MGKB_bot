import sqlite3
from datetime import datetime as d
import os
import sys

MAIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, str(MAIN_DIR))
import config


def sql_operation(func):
    """Декоратор для открытия и закрытия соединения с БД."""
    def wrapper(*args, **kwargs):
        try:
            con = sqlite3.connect(config.PATH_DATABASE)
            cur = con.cursor()
            func(cur, *args, **kwargs)
            con.commit()
        finally:
            con.close()
    return wrapper


@sql_operation
def adding_any_work(cur, user_id, record, users, is_any=False):
    """Создание новой записи в таблице."""
    if user_id in users:
        if is_any:
            work = (d.now(), user_id, record, True)
            cur.execute('''INSERT INTO any_works VALUES(?, ?, ?, ?)''', work)
        else:
            work = (d.now(), user_id, record, False)
            cur.execute('''INSERT INTO any_works VALUES(?, ?, ?, ?)''', work)
    else:
        print(f'{user_id} пользователя нет в юзверях.')


def my_works(user_id):
    """Возвращает список кортежей выполненных работ в этом месяце
    для пользователя, отсортированных по алфавиту"""
    try:
        con = sqlite3.connect(config.PATH_DATABASE)
        cur = con.cursor()
        work = cur.execute('''
            SELECT users.name,
                record,
                COUNT(record)
            FROM any_works
            JOIN users ON any_works.user_id = users.id
            WHERE user_id = (?)
                  AND DATE(created) >= DATE('now', 'start of month')
                  AND is_any_work = False
            GROUP BY record
            ORDER BY record
        ''', (user_id,))
        return [(i[1], i[2]) for i in work]
    finally:
        con.close()


def my_another_works(user_id):
    """Возвращает список кортежей выполненных работ в этом месяце
    для пользователя, отсортированных по алфавиту"""
    try:
        con = sqlite3.connect(config.PATH_DATABASE)
        cur = con.cursor()
        work = cur.execute('''
            SELECT users.name,
                record
            FROM any_works
            JOIN users ON any_works.user_id = users.id
            WHERE user_id = (?)
                  AND DATE(created) >= DATE('now', 'start of month')
                  AND is_any_work = True
            GROUP BY record
            ORDER BY record
        ''', (user_id,))
        return [i[1] for i in work]
    finally:
        con.close()


def all_works_now_month():
    """Возвращает список кортежей выполненных работ в этом месяце
    для всех пользователей"""
    try:
        con = sqlite3.connect(config.PATH_DATABASE)
        cur = con.cursor()
        work = cur.execute('''
            SELECT users.name,
                record,
                COUNT(record)
            FROM any_works
            JOIN users ON any_works.user_id = users.id
            WHERE DATE(created) >= DATE('now', 'start of month')
                  AND is_any_work = False
            GROUP BY users.name, record
            ORDER BY users.name
        ''')
        return [(i[0], i[1], i[2]) for i in work]
    finally:
        con.close()


def all_any_works_now_month():
    """Возвращает список кортежей выполненных работ в этом месяце
    для всех пользователей"""
    try:
        con = sqlite3.connect(config.PATH_DATABASE)
        cur = con.cursor()
        work = cur.execute('''
            SELECT users.name,
                record
            FROM any_works
            JOIN users ON any_works.user_id = users.id
            WHERE DATE(created) >= DATE('now', 'start of month')
                  AND is_any_work = True
            GROUP BY users.name, record
            ORDER BY users.name
        ''')
        return [(i[0], i[1]) for i in work]
    finally:
        con.close()


def all_works_last_month():
    """Возвращает список кортежей выполненных работ в прошлом месяце
    для всех пользователей"""
    try:
        con = sqlite3.connect(config.PATH_DATABASE)
        cur = con.cursor()
        work = cur.execute('''
            SELECT users.name,
                record,
                COUNT(record)
            FROM any_works
            JOIN users ON any_works.user_id = users.id
            WHERE (DATE(created)
                  BETWEEN DATE('now', '-1 months', 'start of month')
                      AND DATE('now', 'start of month', '-1 days'))
                  AND is_any_work = False
            GROUP BY users.name, record
            ORDER BY users.name
        ''')
        return [(i[0], i[1], i[2]) for i in work]
    finally:
        con.close()


def all_any_works_last_month():
    """Возвращает список кортежей выполненных работ в прошлом месяце
    для всех пользователей"""
    try:
        con = sqlite3.connect(config.PATH_DATABASE)
        cur = con.cursor()
        work = cur.execute('''
            SELECT users.name,
                record
            FROM any_works
            JOIN users ON any_works.user_id = users.id
            WHERE (DATE(created)
                  BETWEEN DATE('now', '-1 months', 'start of month')
                      AND DATE('now', 'start of month', '-1 days'))
                  AND is_any_work = True
            GROUP BY users.name, record
            ORDER BY users.name
        ''')
        return [(i[0], i[1]) for i in work]
    finally:
        con.close()
