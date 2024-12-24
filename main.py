from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": "Hello Mohan"}

@app.get("/greet")
async def greeting(age: int, name: Optional[str] = "Guest") -> dict:
    return {"message": f"Hello {name}", "age": age}


class BookCreateModel(BaseModel):
    title: str
    author: str


@app.post("/create_book")
async def create_book(book_data: BookCreateModel) -> dict:
    return { 
        "title": book_data.title,
        "author": book_data.author
    }

@app.get("/get_headers", status_code=201)
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: Optional[str] = Header(None),
    host: Optional[str] = Header(None)
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
    return request_headers


