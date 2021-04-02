from remind.model import session, Reminder, Tag


class ReminderCrud:
    @staticmethod
    def get_all():
        return session.query(Reminder).all()

    @staticmethod
    def save(reminder: Reminder):
        session.add(reminder)
        session.commit()
