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
from dotenv import load_dotenv

load_dotenv()
APP_MODE = os.getenv("APP_MODE")
print(f"APP_MODE : {APP_MODE}")

cache = (
    "test_rmind.db"
    if APP_MODE == "debug"
    else os.path.join(os.path.expanduser("~"), ".rmind.db")
)

engine = create_engine(f"sqlite:///{cache}")
Session = sessionmaker()
Session.configure(bind=engine)
Base = declarative_base()  # type: Any
session = Session()

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
