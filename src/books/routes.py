from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from src.books.schemas import Book, BookUpdateModel
from src.books.book_data import books

book_router = APIRouter()

@book_router.get("/", response_model=list[Book])
async def get_all_books() -> list:
    return books

@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(book: Book) -> dict:
    new_book = book.model_dump()
    books.append(new_book)
    return new_book

@book_router.get("/{book_id}")
async def get_a_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.patch("/{book_id}")
async def update_a_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    
    for book in books:
        if book["id"] == book_id:
            book.update(book_update_data.model_dump())
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
