import re
import shlex
import subprocess
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from xdg.BaseDirectory import load_data_paths
from xdg.DesktopEntry import DesktopEntry


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
