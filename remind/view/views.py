from dataclasses import dataclass

from remind.data.persist import RemindersAndTag, ReminderCrud
from remind.richcontent import ReminderTable, rc
from remind.model import Reminder
from rich.panel import Panel
from random import randint


@dataclass
class ListOfRemindersView:
    reminder_list: list[Reminder]
    verbose: bool

    def render_table(self):
        table = ReminderTable(
            self.reminder_list, verbose=self.verbose, border_style="green"
        )
        rc.print(table.get_table())


@dataclass
class ListOfRemindersAndTagView:
    reminders_and_tags_list: list[RemindersAndTag]
    verbose: bool

    def render_table(self):
        for reminders_and_tag in self.reminders_and_tags_list:
            table = ReminderTable(
                reminders_and_tag.reminders, verbose=self.verbose, border_style="green"
            ).get_table()
            panel = Panel(
                table,
                title=f":label:  [bold white]{reminders_and_tag.tag}",
                title_align="left",
                padding=(1, 3),
                border_style="blue",
            )
            print()

            rc.print(panel, justify="left")


class ViewUtils:
    @staticmethod
    def display_updated(id: int, status: int, verbose: bool):
        if status:
            rc.rule(":+1: [bold white]Updated", style="green")
            reminder: Reminder = ReminderCrud.get_by_id(id)
            table = ReminderTable([reminder], verbose=verbose).get_table()
            rc.print(table)
        else:
            rc.rule(":-1: [bold white]Not Updated", style="yellow")
            rc.print(f"ID {id} does not exist.")

    @staticmethod
    def display_deleted(reminder: Reminder, verbose: bool):
        r: list[Reminder] = [reminder]
        table = ReminderTable(r, verbose=verbose).get_table()
        rc.rule(title=":litter_in_bin_sign: [bold white]Deleted", style="red")
        rc.print(table)

    @staticmethod
    def display_added(reminder: Reminder, verbose: bool):
        r: list[Reminder] = [reminder]
        table = ReminderTable(r, verbose=verbose).get_table()
        rc.rule(title=":card_index_dividers:  [bold white]Saved", style="green")
        rc.print(table)

    @staticmethod
    def display_tag_names(tag_names: list[str]):
        tags = ""
        for tag_name in tag_names:
            tags += f"{tag_name}\n"

        # Try to display these in several columns instead of 1 column
        rc.print(
            Panel(
                tags.strip(),
                expand=False,
                title=":label:  [bold white]Tags",
                title_align="left",
                padding=(1, 3),
                border_style="blue",
            ),
            style="bold white",
        )

    @staticmethod
    def no_opps_update_error():
        rc.rule(title=":robot: [bold white]Attention :robot:", style="yellow")
        rc.print(
            "[bold #05ff05]update[/ bold #05ff05] [bold white]command requires at least one of these options."
        )
        rc.print(
            """\
:arrow_down:   :arrow_down:
Options:
  -u,  --update TEXT       Updated text for specified reminder
  -td, --tag-delete TEXT   Tag to delete association with specified reminder
  -ta, --tag-add TEXT      Tag to add association with specified reminder
  -h,  --help              Show help for update command
            """
        )

    @staticmethod
    def empty_view():
        messages = [
            ":dog2: Wow, such empty! :dog2:",
            ":crescent_moon: Nothing to see here :crescent_moon:",
        ]
        idx = randint(0, len(messages) - 1)
        rc.print(messages[idx])