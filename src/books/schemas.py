from pydantic import BaseModel
from datetime import datetime, date

class BookSchema(BaseModel):
    uid: str
    title: str  
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime


class BookCreateSchema(BaseModel):
    title: str  
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdateSchema(BaseModel):
    title: str  
    author: str
    publisher: str
    page_count: int
    language: str

