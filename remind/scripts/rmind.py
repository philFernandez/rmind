from typing import Union
import click
from remind.model import Reminder
from remind.data import ReminderCrud, RemindersAndTag
from remind.view import (
    ListOfRemindersView,
    ListOfRemindersAndTagView,
    display_deleted,
    display_updated,
)

context_settings = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=context_settings, invoke_without_command=True)
@click.pass_context
@click.option("-t", "--tag", multiple=True, help="Filter by tag(s).")
@click.option("-v", "--verbose", count=True, help="Show more detail in output.")
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
    Add a new note/reminder.

    ex:
    `rmind add -a 'Your note or idea!'`

    Will prompt for note if -a is omitted.
    """
    reminder = Reminder(add)
    if len(tag):
        ReminderCrud.tag_reminder(tag, reminder)
    ReminderCrud.save(reminder)


@cli.command()
@click.argument("id", type=int)
@click.option(
    "-u",
    "--update",
    prompt="Type your updated idea",
    help="Input text directly and skip prompt.",
)
@click.option("-v", "--verbose", count=True, help="Show more detail in output.")
def update(id, update, verbose):
    return_status = ReminderCrud.update_by_id(id, update)
    display_updated(id, return_status, verbose)


@cli.command()
@click.argument("id", type=int)
@click.option("-v", "--verbose", count=True, help="Show more detail in output.")
def delete(id: int, verbose: bool):
    """
    Delete note/reminder with specified id.

    ex:
    `rmind delete 1`
    """
    deleted_reminder: Union[Reminder, None] = ReminderCrud.delete_by_id(id)
    if deleted_reminder is not None:
        display_deleted(deleted_reminder, verbose)


def main():
    cli()