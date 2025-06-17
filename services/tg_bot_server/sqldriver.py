import sqlite3

__APP_SQL_CONFIG_LOCAL_MODULE__ = dict()
__APP_SQL_CONFIG_LOCAL_MODULE__["APPLICATION_SQL_INIT_WORK_SCHEMA"] = False
__APP_SQL_CONFIG_LOCAL_MODULE__["APPLICATION_SQL_INIT_WORK_INSERT"] = False


def initDatabase(appPath: str, encodingFile: str = "utf-8") -> sqlite3.Connection:
    """
    [RUSSIAN]
    Этот метод модуля инициализирует, создает и заполняет базу данных при запуске.
    Возвращает объект подключения к базе данных.
    :param appPath: str - путь в файловой системе к целевому файлу
    :param encodingFile: str - название кодировки целевого файла
    :return: sqlite3.Connection - объект подключения к базе данных.
    """
    global __APP_SQL_CONFIG_LOCAL_MODULE__
    db_connection = sqlite3.connect(appPath + r"\resourses\service.db")
    if __APP_SQL_CONFIG_LOCAL_MODULE__["APPLICATION_SQL_INIT_WORK_SCHEMA"]:
        with open(appPath + r"\config\schem.sql", "r", encoding=encodingFile) as f:
            db_connection.executescript(f.read())
    if __APP_SQL_CONFIG_LOCAL_MODULE__["APPLICATION_SQL_INIT_WORK_INSERT"]:
        with open(appPath + r"\config\data.sql") as f:
            db_connection.executescript(f.read())
    return db_connection
