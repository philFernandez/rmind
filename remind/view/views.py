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
        table = ReminderTable(self.reminder_list, verbose=self.verbose)
        rc.print(table)


@dataclass
class ListOfRemindersAndTagView:
    reminders_and_tags_list: list[RemindersAndTag]
    verbose: bool

    def render_table(self):
        for reminders_and_tag in self.reminders_and_tags_list:
            # rc.rule()
            table = ReminderTable(reminders_and_tag.reminders, verbose=self.verbose)
            panel = Panel(
                table,
                title=f":label:  {reminders_and_tag.tag}",
                title_align="left",
            )
            al = Align(panel, align="center")

            rc.print(al)
