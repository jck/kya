import click

from . import __version__
from . import app

CONTEXT_SETTINGS = {
    'help_option_names': ['-h', '--help']
}


@click.group(invoke_without_command=True,
             context_settings=CONTEXT_SETTINGS
             )
@click.version_option(__version__, '-V', '--version')
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        ctx.invoke(launch)

@cli.command()
def launch():
    app.run()
