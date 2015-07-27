#!/usr/bin/env python
"""Symlink PyQt into the current virtualenv"""

import sys
import subprocess
from pathlib import Path


def site_dir(python):
    cmd = [str(python), '-c',
           'from distutils.sysconfig import get_python_lib\n'
           'print(get_python_lib())']
    return Path(subprocess.check_output(cmd, universal_newlines=True).rstrip())


def link_pyqt(sys_python, venv_python):
    """Symlink the systemwide PyQt/sip into the venv."""
    real_site = site_dir(sys_python)
    venv_site = site_dir(venv_python)

    for f in ['sip.so', 'PyQt5']:
        (venv_site/f).symlink_to(real_site/f)


def main():
    python = 'python{0.major}.{0.minor}'.format(sys.version_info)
    sys_python = Path(sys.real_prefix)/'bin'/python
    venv_python = Path(sys.prefix)/'bin'/python
    link_pyqt(sys_python, venv_python)

if __name__ == '__main__':
    main()
