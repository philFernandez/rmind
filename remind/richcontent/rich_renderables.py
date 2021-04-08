from rich.table import Table
from remind.model import Reminder
from rich.console import Console, RenderableType
from rich import box
from rich.box import Box
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
    box: Box = box.HEAVY_EDGE
    verbose: bool = False
    expand: bool = False
    table = None

    def get_table(self) -> Table:
        self.table = Table(
            "ID",
            "Reminder",
            style=self.style,
            border_style=self.border_style,
            title=self.title,
            caption=f"Count : {len(self.reminders)}",
            show_lines=self.show_lines,
            box=self.box,
            row_styles=self.row_styles,
            expand=self.expand,
        )
        if self.verbose == 1:
            self.table.add_column("Date")
            self.table.add_column("Time")
            for reminder in self.reminders:
                self.table.add_row(
                    f"{reminder.id}",
                    reminder.description,
                    f"{reminder.entry_date.strftime('%D')}",
                    f"{reminder.entry_date.strftime('%I:%m %p')}",
                )
        elif self.verbose >= 2:
            self.table.add_column("Date")
            self.table.add_column("Time")
            self.table.add_column("Tags")
            for reminder in self.reminders:
                tag_names: list[str] = [tag.tag_name for tag in reminder.tags]
                tags = ", ".join(tag_names)
                self.table.add_row(
                    f"{reminder.id}",
                    reminder.description,
                    f"{reminder.entry_date.strftime('%D')}",
                    f"{reminder.entry_date.strftime('%I:%m %p')}",
                    f"{tags}",
                )
        else:
            for reminder in self.reminders:
                self.table.add_row(f"{reminder.id}", reminder.description)

        return self.table

    def get_reminder_cell(self, idx: int) -> RenderableType:
        return self.table.columns[1]._cells[idx]

    def get_reminder_cells(self) -> list[RenderableType]:
        return self.table.columns[1]._cells
