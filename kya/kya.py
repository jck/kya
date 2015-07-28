from fuzzywuzzy.process import extractBests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QLineEdit, QListWidget,
                             QListWidgetItem, QVBoxLayout, QWidget)
from xdg.Config import setIconTheme


class Query(QLineEdit):
    pass

class Results(QListWidget):
    def __init__(self):
        setIconTheme(QIcon.themeName())
        super().__init__()

    def add(self, res):
        item = QListWidgetItem(QIcon(res.icon), res.name)
        item.setData(Qt.UserRole, res)
        self.addItem(item)

class Kya(QWidget):
    def __init__(self, plugin):
        super().__init__()
        self.setWindowTitle('Kya?')
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint |
                            Qt.Tool)

        layout = QVBoxLayout()
        self.query = Query()
        self.results = Results()

        # Hardcode for now
        if plugin == 'applauncher':
            from .plugins import applauncher
            self.all_results = applauncher.apps

        self.query.textChanged.connect(self.handle_query)
        self.query.setFocusPolicy(Qt.StrongFocus)
        self.results.setFocusPolicy(Qt.NoFocus)

        layout.addWidget(self.query)
        layout.addWidget(self.results)

        self.setLayout(layout)
        self.show()

    def keyPressEvent(self, e):
        k = e.key()
        if k == Qt.Key_Escape:
            self.hide()
        elif k == Qt.Key_Tab:
            self.results.setCurrentRow(self.results.currentRow()+1)
        elif k == Qt.Key_Return:
            item = self.results.currentItem().data(Qt.UserRole)
            item.launch()
            self.hide()

        super().keyPressEvent(e)

    def handle_query(self):
        self.results.clear()
        res = extractBests(self.query.text(), self.all_results, 
                           processor=lambda x: x.name, limit=8)
        for r,s in res:
            self.results.add(r)
        self.results.setCurrentRow(0)
