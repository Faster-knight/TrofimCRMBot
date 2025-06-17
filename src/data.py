from json import load, dumps

def writeJsonObject(data: dict, pathFile: str, encoding_name: str = "utf-8") -> None:
    with open(pathFile, "w", encoding=encoding_name) as f:
        dumps(fp=f, obj=data)


def readJsonObject(pathFile: str, encoding_name: str = "utf-8") -> dict | list:
    with open(pathFile, "r", encoding=encoding_name) as f:
        data = load(f)
    return data


def writeEnvData(data: dict, pathFile: str, encoding_name: str = "utf-8") -> None:
    __temp = str("")
    for k, v in data:
        __temp += f"{k}={v}\n"
    with open(pathFile, "w", encoding=encoding_name) as f:
        f.write(__temp)
        del __temp
        del k
        del v


def readEnvFile(pathFile: str, encoding_name: str = "utf-8") -> dict:
    """
    [RUSSIAN]
    Этот метод парсит и получает данные из .env файла
    возвращая объект словаря.
    :param pathFile: str - путь к целевому файлу в файловой системе.
    :param encoding_name: str - название кодировки в которой должен находится целевой файл.
    :return: dict - данные полученные из файла.
    """
    with open(pathFile, "r", encoding=encoding_name) as f:
        __temp = f.read()
    __sp = __temp.split("\n")
    del __temp
    t = dict()
    for line in __sp:
        __temp = line.split("=")
        t[__temp[0]] = __temp[1]
    del __temp
    del __sp
    return t
