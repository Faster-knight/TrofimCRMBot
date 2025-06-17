from PyQt6.QtCore import QRect
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QMainWindow


class BaseApplicationWidget(QWidget):
    """
    [RUSSIAN]
    Данный класс является базовым классом элемента графического интерфейса
    или компонента графического интерфейса в приложении. В основном он
    используется для создания дочерних графических компонентов в качестве
    родительского класса.

    Класс создает внутри себя родительский класс QWidget и запускает
    метод setupUI который настраивает графический компонент индивидуально
    в классах наследниках.
    """
    def __init__(self, parentWidget=None, *args, **kwargs):
        super().__init__(parent=parentWidget)
        self.setupUI()

    def setupUI(self, *args, **kwargs):
        pass


class MainApplicationWindow(QMainWindow):
    """
    [RUSSIAN]
    Этот класс является классом корневого графического интерфейса в приложении.
    Наследуется от QMainWindow класса. Нигде в других классах не используется.
    """
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