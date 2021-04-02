from remind.richcontent import ReminderTable, rc
from remind.model import Reminder, session
from rich.layout import Layout
from rich.panel import Panel
from rich import box


# run this file directly to run this fun (python remind/scripts/rmind.py)
def entry_test():
    reminders: list[Reminder] = [
        Reminder("Do a thing"),
        Reminder("Do a stuff"),
        Reminder("Do a thing and stuff"),
    ]
    for reminder in reminders:
        session.add(reminder)
        session.commit()

    tbl = ReminderTable(
        reminders,
        style="bold green",
        border_style="blue",
        title="Reminder Table",
        row_styles=["blue on green", "green on blue"],
        verbose=True,
        expand=True,
        box=box.SIMPLE,
        show_lines=True,
    )

    tbl2 = ReminderTable(
        reminders,
        style="bold green",
        border_style="blue",
        title="Reminder Table",
        row_styles=["blue on green", "green on blue"],
        box=box.SIMPLE,
    )
    lo = Layout(name="root")
    lo.split_row(
        Layout(Panel(tbl, border_style="green"), name="left"),
        Layout(Panel(tbl2, border_style="blue"), name="right"),
    )
    rc.rule()
    rc.print(lo, height=14)
    rc.print(tbl2, justify="center")


def entry_point():
    entry_test()


if __name__ == "__main__":
    entry_test()