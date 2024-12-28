from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from src.books.schemas import BookSchema, BookUpdateSchema, BookCreateSchema
from src.books.service import BookService
from src.db.main import get_session

book_router = APIRouter()
book_service = BookService()

@book_router.get("/", response_model=list[BookSchema])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books

@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=BookSchema)
async def create_a_book(book: BookCreateSchema, session: AsyncSession = Depends(get_session)):
    new_book = await book_service.create_a_book(book, session)
    return new_book

@book_router.get("/{book_id}", response_model=BookSchema)
async def get_a_book(book_id: str, session: AsyncSession = Depends(get_session)):
    book = await book_service.get_a_book(book_id, session)
    if book:
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.patch("/{book_id}", response_model=BookSchema)
async def update_a_book(book_id: str, book_update_data: BookUpdateSchema, session: AsyncSession = Depends(get_session)):
    updated_book = await book_service.update_a_book(book_id, book_update_data, session)
    if updated_book:
        return updated_book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    

@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id: str, session: AsyncSession = Depends(get_session)):
    is_deleted = await book_service.delete_a_book(book_id, session)
    if is_deleted:
        return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
