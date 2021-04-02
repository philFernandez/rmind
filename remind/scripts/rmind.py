from remind.richcontent import ReminderTable
from remind.model import Reminder


def entry_point():
    reminders: list[Reminder] = [
        Reminder("1", "Do a thing"),
        Reminder("2", "Do a stuff"),
        Reminder("3", "Do a thing and stuff"),
    ]
    tbl = ReminderTable(
        "Test Table", color="green", border_color="blue", reminders=reminders
    )

    tbl.print_table()
