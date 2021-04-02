from remind.richcontent import ReminderTable, rc
from remind.model import Reminder


def entry_point():
    reminders: list[Reminder] = [
        Reminder("1", "Do a thing"),
        Reminder("2", "Do a stuff"),
        Reminder("3", "Do a thing and stuff"),
    ]
    tbl = ReminderTable(
        reminders,
        style="bold green",
        border_style="blue",
        title="Reminder Table",
        row_styles=["blue on green", "green on blue"],
    )
    rc.rule()
    rc.print(tbl, justify="center")
