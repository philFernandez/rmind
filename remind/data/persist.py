from sqlalchemy.orm.relationships import RelationshipProperty
from remind.model import Reminder, Tag, reminder_tag, session
from typing import NamedTuple

# from collections import namedtuple

# RemindersAndTag = namedtuple("RemindersAndTag", ["reminders"], "tag")


class RemindersAndTag(NamedTuple):
    reminders: list[Reminder]
    tag: str


class ReminderCrud:
    @staticmethod
    def get_all() -> list[Reminder]:
        return session.query(Reminder).all()

    @staticmethod
    def save(reminder: Reminder):
        session.add(reminder)
        session.commit()

    @staticmethod
    def delete_by_id(id: int):
        reminder: Reminder = session.query(Reminder).get(id)
        if reminder is not None:
            for tag in reminder.tags:
                reminder_tag_query = (
                    # check association table to check if tags associated with deleted reminder
                    # are associated with any other reminders. If they're not, delete them.
                    session.query(reminder_tag)
                    .filter_by(tag_id=tag.id)
                    .all()
                )
                if len(reminder_tag_query) == 1:
                    # Tag is only associated with one reminder, the one being deleted, so delete tag too
                    session.delete(tag)

            session.delete(reminder)
            session.commit()

            return reminder

        else:
            return None

    @staticmethod
    def filter_by_tags(tags: tuple[str]) -> list[RemindersAndTag]:
        reminders_and_tag: list[RemindersAndTag] = []
        for tag in tags:
            try:
                tag_id = session.query(Tag.id).filter_by(tag_name=tag).first()[0]
            except TypeError:
                print(f"tag {tag} does not exist.")
                continue
            reminders_and_tag.append(
                RemindersAndTag(
                    session.query(Reminder)
                    .join(reminder_tag)
                    .filter(reminder_tag.c.tag_id == tag_id)
                    .filter(reminder_tag.c.reminder_id == Reminder.id)
                    .all(),
                    tag,
                )
            )
        return reminders_and_tag

    @staticmethod
    def tag_reminder(tags: list[Tag], reminder: Reminder):
        for tag in tags:
            queried_tag = session.query(Tag).filter_by(tag_name=tag).first()
            if queried_tag is None:
                queried_tag = Tag(tag_name=tag)

            reminder.tags.append(queried_tag)
