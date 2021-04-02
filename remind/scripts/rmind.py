from remind.richcontent import ReminderTable, rc
from remind.model import Reminder
from rich.layout import Layout
from rich.panel import Panel


# run this file directly to run this fun (python remind/scripts/rmind.py)
def entry_test():
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
        verbose=True,
        expand=True,
    )
    tbl2 = ReminderTable(
        reminders,
        style="bold green",
        border_style="blue",
        title="Reminder Table",
        row_styles=["blue on green", "green on blue"],
    )
    lo = Layout(name="root")
    lo.split_row(
        Layout(Panel(tbl, border_style="green"), name="left"),
        Layout(Panel(tbl2, border_style="blue"), name="right"),
    )
    rc.rule()
    rc.print(lo, height=14)
    rc.print(tbl2, justify="center")


if __name__ == "__main__":
    entry_test()