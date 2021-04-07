import os
from datetime import datetime
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
    create_engine,
)
from typing import Any
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import dotenv

# Read .env file to determine if we are in "test" mode
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
APP_MODE = os.getenv("APP_MODE")

# If we are in "test" mode then use temp ".test.db" for operations.
# Program execution will take place from "test/test_rmind.py".
# If we are not in "test" mode ".rmind.db" in the user's home
# directory is used for normal operations.
cache = (
    ".test.db"
    if APP_MODE == "test"
    else os.path.join(os.path.expanduser("~"), ".rmind.db")
)

engine = create_engine(f"sqlite:///{cache}")
Session = sessionmaker()
Session.configure(bind=engine)
Base = declarative_base()  # type: Any
session = Session()


# Association table for many-to-many relationship between Reminder + Tag entities.
reminder_tag = Table(
    "reminder_tag",
    Base.metadata,
    Column("reminder_id", Integer, ForeignKey("reminder.id")),
    Column("tag_id", Integer, ForeignKey("tag.id")),
)


class Reminder(Base):
    __tablename__ = "reminder"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False, unique=True)
    entry_date = Column(DateTime, nullable=False)
    tags = relationship("Tag", secondary=reminder_tag, back_populates="reminders")

    def __init__(self, description: str):
        self.description = description
        self.entry_date = datetime.now()

    def __repr__(self):
        return f"Reminder (id: {self.id}, desc: {self.description}, entry_date: {self.entry_date})"


class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True)
    tag_name = Column(String, nullable=False, unique=True)
    reminders = relationship(
        "Reminder", secondary="reminder_tag", back_populates="tags"
    )

    def __repr__(self):
        return f" Tag (id: {self.id}, tag_name: {self.tag_name}) "


Base.metadata.create_all(engine)

if __name__ == "__main__":
    print("models.py")
