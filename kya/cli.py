import sys

import click
from PyQt5.QtWidgets import QApplication

from .app import Kya


@click.command()
@click.argument('plugin')
def main(plugin):
    app = QApplication([])
    ui = Kya(plugin)
    sys.exit(app.exec_())
