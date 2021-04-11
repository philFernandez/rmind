from remind.model import Reminder, Tag, reminder_tag, session
from typing import NamedTuple

# !! DELETE THESE BEFORE PACKAGING !!
# ** Also delete the places that use these **
from rich.traceback import install
from rich.console import Console

install()
rp = Console()
# !! ============================== !!


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
    def remove_tag_from_reminder(id: int, tag_name: str):
        tag = session.query(Tag).filter_by(tag_name=tag_name).first()
        reminder = session.query(Reminder).filter_by(id=id).first()
        reminder.tags.remove(tag)
        tag_association = session.query(reminder_tag).filter_by(tag_id=tag.id).all()
        if not len(tag_association):
            session.delete(tag)
        session.commit()

    # ? <== === === === === === === ==>
    # ! This uses 'tag_reminder' as a helper to add a tag to a reminder
    # ! Want to use this function in conjuntion with 'remove_tag_from_reminder'
    # ! For updating a tag to an existing reminder. i.e. to remove a tag and
    # ! replace it with a new one.
    # * <- --- --- --- --- --- --- --- ->
    @staticmethod
    def tag_reminder_by_id(id: int, tag_name: str):
        reminder = session.query(Reminder).filter_by(id=id).first()
        ReminderCrud.tag_reminder([tag_name], reminder)
        session.commit()

    @staticmethod
    def get_by_id(id: int) -> Reminder:
        reminder: Reminder = session.query(Reminder).filter(Reminder.id == id).first()
        return reminder

    @staticmethod
    def update_by_id(id: int, new_description: str) -> int:
        query_found = (
            session.query(Reminder)
            .filter(Reminder.id == id)
            .update({"description": new_description}, synchronize_session="fetch")
        )
        if query_found:
            session.commit()
        return query_found

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
    def tag_reminder(tags: list[str], reminder: Reminder):
        for tag in tags:
            queried_tag = session.query(Tag).filter_by(tag_name=tag).first()
            if queried_tag is None:
                queried_tag = Tag(tag_name=tag)

            reminder.tags.append(queried_tag)
