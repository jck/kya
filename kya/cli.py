import asyncio
import sys

import click
from PyQt5.QtWidgets import QApplication
from quamash import QEventLoop

from .app import Kya

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    ctx.obj = QApplication([])
    if ctx.invoked_subcommand is None:
        ctx.invoke(launch)

@cli.command()
@click.pass_obj
def launch(app):
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    with loop:
        widget = Kya('applauncher')
        loop.run_forever()
    sys.exit(app.exec_())
