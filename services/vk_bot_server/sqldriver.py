import sqlite3
from symtable import Function


def initDatabase(appPath: str) -> sqlite3.Connection:
    db_connection = sqlite3.connect(appPath + r"\resourses\service.db")
    return db_connection


def createMapping(func: Function):
    def wrapper(*args, **kwargs):
        func()
    return wrapper
