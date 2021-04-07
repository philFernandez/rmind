from dataclasses import dataclass

from rich.table import Table
from remind.data.persist import RemindersAndTag
from remind.richcontent import ReminderTable, rc
from remind.model import Reminder, Tag
from rich.panel import Panel


@dataclass
class ListOfRemindersView:
    reminder_list: list[Reminder]
    verbose: bool

    def render_table(self):
        table = ReminderTable(
            self.reminder_list, verbose=self.verbose, border_style="green"
        ).get_table()
        rc.print(table)


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


def display_updated(id: int, updated_text: str, status: int):
    if status:
        rc.rule(":+1: [bold white]Updated", style="green")
        table = Table("ID", "Reminder")
        table.add_row(f"{id}", updated_text)
        rc.print(table)
    else:
        rc.rule(":-1: [bold white]Not Updated", style="yellow")
        rc.print(f"ID {id} does not exist.")


def display_deleted(reminder: Reminder, verbose: bool):
    r: list[Reminder] = [reminder]
    table = ReminderTable(r, verbose=verbose)
    rc.rule(title=":litter_in_bin_sign: [bold white]Deleted", style="red")
    rc.print(table.get_table())