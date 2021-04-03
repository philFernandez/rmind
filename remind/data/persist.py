from sqlalchemy.orm.relationships import RelationshipProperty
import typing as t
from remind.model import Reminder, Tag, session


class ReminderCrud:
    @staticmethod
    def get_all() -> list[Reminder]:
        return session.query(Reminder).all()

    @staticmethod
    def save(reminder: Reminder):
        session.add(reminder)
        session.commit()

    @staticmethod
    def tag_reminder(tags: list[Tag], reminder: Reminder):
        for tag in tags:
            queried_tag = session.query(Tag).filter_by(tag_name=tag).first()
            if queried_tag is None:
                queried_tag = Tag(tag_name=tag)

            reminder.tags.append(queried_tag)
