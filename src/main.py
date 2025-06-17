__APP_PATH__ = str()
__APP_CONFIG__ = dict()
__APP_DEVICE_INFO__ = dict()
__APP_THREAD_WORK__ = {
    "ui": True,
    "broadcast": True
}

from PyQt6.QtCore import QRect

from src.ui import MainApplicationWindow

if __name__ == '__main__':
    from PyQt6.QtWidgets import QApplication
    import sys as __sys
    import threading as __thr
    import platform as __plt
    import os as __os

    app = QApplication(__sys.argv)
    __APP_DEVICE_INFO__["CPU_COUNT"] = __os.cpu_count()
    __APP_DEVICE_INFO__["OS_NAME"] = __plt.system()
    __APP_DEVICE_INFO__["OS_VERSION"] = __plt.version()
    __APP_CONFIG__["APPLICATION_WORK_MODE"] = "dev"
    __APP_PATH__ = __os.path.dirname(__file__)
    if __APP_CONFIG__["APPLICATION_WORK_MODE"] == "dev":
        print("Start program with this parameters:\n-----------------------------------\nConfig:")
        print(__APP_CONFIG__)
        print("-----------------------------------\nDevice information:")
        print(__APP_DEVICE_INFO__)
        print("-----------------------------------\nApp thread init start work information:")
        print(__APP_THREAD_WORK__)


    def ui_handle() -> None:
        """
        [RUSSIAN]
        Это второстепенный поток приложения который
        управляет графическим интерфейсом.
        :return: None
        """
        global app
        global __APP_CONFIG__
        if __APP_CONFIG__["APPLICATION_WORK_MODE"] == "dev":
            print("Start uin_thread work!")
        window = MainApplicationWindow(
            QRect(0, 0, 300, 300),
            "",
            __APP_PATH__ + r"\img\img_ui_logo_lion.png",
            None
        )
        window.show()
        __sys.exit(app.exec())


    def main_handle():
        """
        [RUSSIAN]
        Это первостепенный поток приложения который
        работает с входными данными от ботов и
        аккаунтов в социальных сетях.
        :return: None
        """
        global __APP_CONFIG__
        if __APP_CONFIG__["APPLICATION_WORK_MODE"] == "dev":
            print("Start main_thread work!")
        while 1:
            print(0)


    def broadcast_handle():
        """
        [RUSSIAN]
        Это второстепенный поток приложения который
        управляет оповещениями ботов от имени пользователя.
        :return: None
        """
        global __APP_CONFIG__
        if __APP_CONFIG__["APPLICATION_WORK_MODE"] == "dev":
            print("Start broadcast_thread work!")
        while 1:
            print(1)


    ui_thread = __thr.Thread(name="ui_thread", daemon=False, target=ui_handle)
    main_thread = __thr.Thread(name="main_thread", daemon=True, target=main_handle)
    broadcast_thread = __thr.Thread(name="broadcast_thread" , daemon=False, target=broadcast_handle)
    main_thread.start()
    ui_thread.run()
    broadcast_thread.run()
