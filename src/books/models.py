from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.mysql as mysql
from datetime import datetime, date
import uuid

class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: uuid.UUID = Field(
        sa_column=Column(
            mysql.CHAR(36),
            primary_key=True,
            nullable=False,
            default=lambda: str(uuid.uuid4()),
        )
    )
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime = Field(
        sa_column=Column(
            mysql.DATETIME,
            default=datetime.now,
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            mysql.DATETIME,
            default=datetime.now,
        )
    )

    def __repr__(self) -> str:
        return f"<Book(uid={self.uid}, title={self.title}, author={self.author})>"
