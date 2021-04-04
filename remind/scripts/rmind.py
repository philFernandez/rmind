import click
from remind.model import Reminder
from remind.data import ReminderCrud, RemindersAndTag

context_settings = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=context_settings, invoke_without_command=True)
@click.pass_context
@click.option("-t", "--tag", multiple=True, help="Filter by tag(s).")
@click.option("-v", "--verbose", is_flag=True, help="Show more detail in output.")
def cli(ctx, tag, verbose):
    if ctx.invoked_subcommand is None:
        reminders: list[Reminder] = ReminderCrud.get_all()
        if not len(tag):  # if no "-t" options given

            if verbose:
                click.echo("VERBOSE OUTPUT")
                for reminder in reminders:
                    click.echo(reminder.id)
                    click.echo(reminder.description)
                    click.echo(reminder.entry_date)
                    click.echo("-" * 50)
            else:
                for reminder in reminders:
                    click.echo(reminder.id)
                    click.echo(reminder.description)
                    click.echo(reminder.entry_date)
                    click.echo("-" * 50)
        else:
            tagged_reminders: list[RemindersAndTag] = ReminderCrud.filter_by_tags(tag)
            for tagged_reminder in tagged_reminders:
                click.echo(tagged_reminder.reminders)
                click.echo(tagged_reminder.tag)


@cli.command()
@click.option(
    "-a",
    "--add",
    prompt="Type your idea",
    help="Input text directly and skip prompt.",
)
@click.option("-t", "--tag", help="Add tag(s) to your note.", multiple=True)
def add(add, tag):
    """
    rmind add [-a] <your idea/reminder>

    prompts for input is -a is ommited.
    """
    reminder = Reminder(add)
    if len(tag):
        ReminderCrud.tag_reminder(tag, reminder)
    ReminderCrud.save(reminder)


def main():
    cli()