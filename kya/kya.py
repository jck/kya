import re
import shlex
import subprocess
import sys
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QLineEdit, QListWidget,
                             QListWidgetItem, QVBoxLayout, QWidget)
from xdg.BaseDirectory import load_data_paths
from xdg.DesktopEntry import DesktopEntry


class Query(QLineEdit):
    pass


class App:
    def __init__(self, d):
        self._d = DesktopEntry(str(d))

    @property
    def name(self):
        return self._d.getName()

    @property
    def icon(self):
        return self._d.getIcon()

    def launch(self):
        c = shlex.split(re.sub('%[fFuUdDnNickvm]', '', self._d.getExec()))
        subprocess.Popen(c, close_fds=True, stdin=None, stdout=None,
                         stderr=None)


class Results(QListWidget):
    def __init__(self):
        self.apps = []
        for d in load_data_paths('applications'):
            for a in Path(d).glob('*.desktop'):
                self.apps.append(App(a))
        super().__init__()

    def add(self, app):
        item = QListWidgetItem(QIcon.fromTheme(app.icon), app.name)
        item.setData(Qt.UserRole, app)
        self.addItem(item)


class Kya(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Kya?')
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint |
                            Qt.Tool)

        layout = QVBoxLayout()
        self.query = Query()
        self.results = Results()

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


def cli():
    app = QApplication(sys.argv)
    kya = Kya()
    sys.exit(app.exec_())
