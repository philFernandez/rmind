from rich.table import Table
from remind.model import Reminder
from rich.console import Console, ConsoleOptions, RenderResult
from rich import box
from dataclasses import dataclass, field

rc = Console()


@dataclass
class ReminderTable:
    reminders: list[Reminder]
    row_styles: list[str] = field(default_factory=list)
    style: str = ""
    border_style: str = ""
    title: str = ""
    show_lines: bool = False
    box = box.HEAVY_EDGE

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        tbl = Table(
            "ID",
            "Reminder",
            style=self.style,
            border_style=self.border_style,
            title=self.title,
            caption=f"Count : {len(self.reminders)}",
            show_lines=self.show_lines,
            box=self.box,
            row_styles=self.row_styles,
        )
        for reminder in self.reminders:
            tbl.add_row(reminder.id, reminder.reminder)
        yield tbl
