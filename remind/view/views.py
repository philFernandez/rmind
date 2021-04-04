from dataclasses import dataclass
from remind.richcontent import ReminderTable, rc
from remind.model import Reminder, Tag


@dataclass
class ListOfRemindersView:
    reminder_list: list[Reminder]
    verbose: bool

    def render_table(self):
        table = ReminderTable(self.reminder_list, verbose=self.verbose)
        rc.print(table)


class ListOfRemindersAndTagView:
    pass