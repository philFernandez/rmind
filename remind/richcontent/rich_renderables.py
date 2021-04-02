from rich.table import Table
from remind.model import Reminder
from rich.console import Console

rc = Console()


class ReminderTable:
    def __init__(
        self,
        title: str,
        color="white",
        border_color="white",
        verbose_table=False,
        reminders: list[Reminder] = [],
    ):
        self.title: str = title
        self.border_color: str = border_color
        self.color: str = color
        self.reminders = reminders
        self.t = Table(
            "ID", "Reminder", border_style=self.border_color, style=self.color
        )
        if verbose_table:
            for reminder in reminders:
                self.t.add_row(reminder.id, reminder.reminder)
        else:
            for reminder in reminders:
                self.t.add_row(reminder.id, reminder.reminder)

    def print_table(self):
        rc.print(self.t)

    def __repr__(self):
        return f"ReminderTable (title: {self.title})"
