import asyncio
import sys

import click
from PyQt5.QtWidgets import QApplication
from quamash import QEventLoop

from .app import Kya


@click.command()
@click.argument('plugin')
def main(plugin):
    app = QApplication([])
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    with loop:
        widget = Kya(plugin)
        loop.run_forever()
    sys.exit(app.exec_())
