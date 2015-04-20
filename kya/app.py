from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QLineEdit, QListWidget,
                             QListWidgetItem, QVBoxLayout, QWidget)

from .plugins import applauncher

class Query(QLineEdit):
    pass

class Kya(QWidget):
    def __init__(self, plugin):
        super().__init__()
        self.setWindowTitle('Kya?')
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint |
                            Qt.Tool)

        layout = QVBoxLayout()
        self.query = Query()
        # Hardcode for now
        if plugin == 'applauncher':
            self.results = applauncher.Results()
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
            QApplication.quit()
        elif k == Qt.Key_Tab:
            self.results.setCurrentRow(self.results.currentRow()+1)
        elif k == Qt.Key_Return:
            item = self.results.currentItem().data(Qt.UserRole)
            item.launch()
            QApplication.quit()

        super().keyPressEvent(e)

    def handle_query(self):
        self.results.clear()
        q = self.query.text().lower()
        res = (a for a in self.results.apps if a.name.lower().startswith(q))
        for r in res:
            self.results.add(r)
