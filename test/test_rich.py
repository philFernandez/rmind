from remind.model import Reminder
from remind.richcontent import ReminderTable


class TestReminderTable:
    def test_table_entry(self):
        reminder_description = "THIS IS A TEST"
        reminder = Reminder(reminder_description)
        table = ReminderTable([reminder])
        table.get_table()
        assert table.get_reminder_cell(0) == "THIS IS A TEST"