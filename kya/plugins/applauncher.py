import re
import shlex
import subprocess
from pathlib import Path

from xdg.BaseDirectory import load_data_paths
from xdg.DesktopEntry import DesktopEntry
from xdg.IconTheme import getIconPath


class App:
    def __init__(self, d):
        self._d = DesktopEntry(str(d))
        self.name = self._d.getName()
        self.icon = getIconPath(self._d.getIcon())
        self.exe = shlex.split(re.sub('%[fFuUdDnNickvm]', '', self._d.getExec()))

    def launch(self):
        subprocess.Popen(self.exe, close_fds=True, stdin=None, stdout=None,
                         stderr=None)


apps = []
for d in load_data_paths('applications'):
    for a in Path(d).glob('*.desktop'):
        apps.append(App(a))
