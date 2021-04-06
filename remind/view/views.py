from dataclasses import dataclass
from remind.data.persist import RemindersAndTag
from remind.richcontent import ReminderTable, rc
from remind.model import Reminder, Tag
from rich.panel import Panel
from rich.align import Align


@dataclass
class ListOfRemindersView:
    reminder_list: list[Reminder]
    verbose: bool

    def render_table(self):
        table = ReminderTable(self.reminder_list, verbose=self.verbose).get_table()
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


def display_deleted(reminder: Reminder, verbose: bool):
    r: list[Reminder] = [reminder]
    table = ReminderTable(r, verbose=verbose)
    rc.rule(title=":litter_in_bin_sign: [bold white]Deleted", style="red")
    rc.print(table.get_table())