from datetime import datetime


class Reminder:
    def __init__(self, id: str, reminder: str):
        self.id = id
        self.reminder = reminder
        self.entry_date = datetime.now()

    def __repr__(self):
        return f"Reminder (id: {self.id}, reminder: {self.reminder})"