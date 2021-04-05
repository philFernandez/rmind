import click
from remind.model import Reminder
from remind.data import ReminderCrud, RemindersAndTag
from remind.view import ListOfRemindersView, ListOfRemindersAndTagView

context_settings = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=context_settings, invoke_without_command=True)
@click.pass_context
@click.option("-t", "--tag", multiple=True, help="Filter by tag(s).")
@click.option("-v", "--verbose", is_flag=True, help="Show more detail in output.")
def cli(ctx, tag, verbose):
    if ctx.invoked_subcommand is None:
        if not len(tag):  # if no "-t" options given
            reminders: list[Reminder] = ReminderCrud.get_all()
            ListOfRemindersView(reminders, verbose).render_table()
        else:
            reminders_and_tags: list[RemindersAndTag] = ReminderCrud.filter_by_tags(tag)
            ListOfRemindersAndTagView(reminders_and_tags, verbose).render_table()


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