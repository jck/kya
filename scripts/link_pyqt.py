#!/usr/bin/env python
"""Symlink PyQt into the current virtualenv"""

import sys
import subprocess
from pathlib import Path


def site_dir(prefix):
    executable = str(Path(prefix) / 'bin/python')
    cmd = [executable, '-c',
           'from distutils.sysconfig import get_python_lib\n'
           'print(get_python_lib())']
    return Path(subprocess.check_output(cmd, universal_newlines=True).rstrip())


def link_pyqt(sys_prefix, venv_prefix):
    """Symlink the systemwide PyQt/sip into the venv."""
    real_site = site_dir(sys_prefix)
    venv_site = site_dir(venv_prefix)

    for f in ['sip.so', 'PyQt5']:
        (venv_site/f).symlink_to(real_site/f)


def main():
    link_pyqt(sys.real_prefix, sys.prefix)

if __name__ == '__main__':
    main()
