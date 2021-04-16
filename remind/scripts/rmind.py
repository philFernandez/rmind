from typing import Union
import click
from remind.model import Reminder
from remind.data import ReminderCrud, RemindersAndTag
from remind.view import ListOfRemindersView, ListOfRemindersAndTagView, ViewUtils

context_settings = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=context_settings, invoke_without_command=True)
@click.pass_context
@click.option("-t", "--tag", multiple=True, help="Filter by tag(s).")
@click.option("-v", "--verbose", count=True, help="Show more detail in output.")
def cli(ctx, tag, verbose):
    """
    Running `rmind [OPTIONS]` without any command returns saved data.

    Try `rmind COMMAND -h` for help with specific command.
    """
    if ctx.invoked_subcommand is None:
        if not len(tag):  # if no "-t" options given
            reminders: list[Reminder] = ReminderCrud.get_all()
            if len(reminders):
                ListOfRemindersView(reminders, verbose).render_table()
            else:
                ViewUtils.empty_view()
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
@click.option(
    "-v", "--verbose", count=True, help="Show more detail in output. -v or -vv"
)
def add(add, tag, verbose):
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
    ViewUtils.display_added(reminder, verbose)


@cli.command()
@click.argument("id", type=int)
@click.option("-u", "--update", type=str, help="Update contents of specified reminder.")
@click.option(
    "-td", "--tag-delete", type=str, help="Remove a tag from specified reminder."
)
@click.option("-ta", "--tag-add", type=str, help="Add a new tag to specified reminder.")
# ! Maybe VERBOSE doesn't make sense here??
# // verbose
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Show more detail in output. -v or -vv",
)
def update(id, update, verbose, tag_delete, tag_add):
    """
    Update a reminder specified by its ID.

    ex:
    `rmind update 1 -u 'Some updated note'`,

    `rmind update 1 -ta new_tag`,

    `rmind update 1 -td tag_to_remove`,

    Will prompt for update if -u is omitted.
    """
    if update is not None:
        return_status = ReminderCrud.update_by_id(id, update)
        ViewUtils.display_updated(id, return_status, verbose)
    if tag_add is not None:
        ReminderCrud.tag_reminder_by_id(id, tag_add)
    if tag_delete is not None:
        ReminderCrud.remove_tag_from_reminder(id, tag_delete)

    if update is tag_add is tag_delete is None:
        ViewUtils.no_opps_update_error()


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
        ViewUtils.display_deleted(deleted_reminder, verbose)


@cli.command()
def tags():
    """
    List all tags currently saved.
    """
    all_tags = ReminderCrud.get_all_tag_names()
    ViewUtils.display_tag_names(all_tags)


def main():
    cli()