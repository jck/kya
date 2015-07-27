import re
import shlex
import subprocess
from functools import partial
from pathlib import Path

from collections import namedtuple

from xdg.BaseDirectory import load_data_paths
from xdg.DesktopEntry import DesktopEntry
from xdg.IconTheme import getIconPath


class App(namedtuple('App', 'name icon launch')):
    def __new__(cls, desk):
        desk = DesktopEntry(str(a))
        name = desk.getName()
        icon = getIconPath(desk.getIcon())
        exe = shlex.split(re.sub('%[fFuUdDnNickvm]', '', desk.getExec()))
        launch = partial(subprocess.Popen, exe)
        return super().__new__(cls, name, icon, launch)


apps = []
for d in load_data_paths('applications'):
    for a in Path(d).glob('*.desktop'):
        apps.append(App(a))
