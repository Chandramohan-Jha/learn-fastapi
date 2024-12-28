from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.mysql as mysql
from datetime import datetime
import uuid

class User(SQLModel, table=True):
  __tablename__ = "user"
  uid: uuid.UUID = Field(
    sa_column=Column(
      mysql.CHAR(36),
      primary_key=True,
      nullable=False,
      default=lambda: str(uuid.uuid4()),
    )
  )
  username: str
  email: str
  password: str
  first_name: str
  last_name: str
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
    return f"<User(uid={self.uid}, username={self.username}, email={self.email})>"