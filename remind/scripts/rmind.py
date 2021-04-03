import click
from remind.model import Reminder
from remind.data import ReminderCrud

context_settings = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=context_settings, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        reminders: list[Reminder] = ReminderCrud.get_all()
        for reminder in reminders:
            click.echo(reminder.id)
            click.echo(reminder.description)
            click.echo(reminder.entry_date)
            click.echo("-" * 50)


@cli.command()
@click.option(
    "-a",
    "--add",
    prompt="Type your idea",
    help="use the -a option followed by quote wrapped text to save an entry",
)
def add(add):
    """
    'rmind add [-a] <your idea/reminder>'

    If [-a] is ommitted then 'rmind add'
    will prompt for your input.
    """
    reminder = Reminder(add)
    ReminderCrud.save(reminder)


def main():
    cli()