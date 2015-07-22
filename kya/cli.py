import asyncio
import sys

import click
from PyQt5.QtWidgets import QApplication
from quamash import QEventLoop

from . import __version__
from .app import Kya

CONTEXT_SETTINGS = {
    'help_option_names': ['-h', '--help']
}


@click.group(invoke_without_command=True,
             context_settings=CONTEXT_SETTINGS
             )
@click.version_option(__version__, '-V', '--version')
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
