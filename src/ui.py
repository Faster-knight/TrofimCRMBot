from PyQt6.QtCore import QRect
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QMainWindow

from data import readEnvFile


class BaseApplicationWidget(QWidget):
    def __init__(self, parentWidget=None, *args, **kwargs):
        super().__init__(parent=parentWidget)
        self.setupUI()

    def setupUI(self, *args, **kwargs):
        pass


class MainApplicationWindow(QMainWindow):
    def __init__(
            self,
            geometry: QRect,
            windowTitle: str,
            pathIcon: str,
            styleSheet: str | None
    ) -> None:
        super().__init__()
        # Setup ui settings widgets
        if styleSheet:
            self.setStyleSheet(styleSheet=styleSheet)
        self.setGeometry(geometry)
        self.setWindowTitle(windowTitle)
        self.setWindowIcon(QIcon(pathIcon))
        # Setup child widgets