from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book:
    id: int
    title: str
    description: str
    author: str
    rating: int

    def __init__(self, id, title, description, author, rating) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.rating = rating
        
class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed to create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "JK Rowling",
                "description": "A new description of our book",
                "rating": 5
            }
        }
    }


BOOKS = [
    Book(1, "Computer Science Pro", "A must have", "JJ Smith", 5),
    Book(2, "Be Fast with FAST API", "Great one!", "codingwithroby", 4),
    Book(3, "Master Endpoints", "Could be better", "codingwithroby", 3),
    Book(4, "HP1", "Classic", "JK Rowling", 5),
    Book(5, "HP2", "Another must have", "JK Rowling", 4),
    Book(6, "HP3", "Legendary!", "JK Rowling", 2),
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book_id == book.id:
            return book
        
@app.get("/books/")
async def read_book_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
            
    return books_to_return

@app.post("/create_book")
async def create_book(book_request: BookRequest) -> None:
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)
    
@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = Book(**book.model_dump())
            
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break    
    
def find_book_id(book: Book) -> Book:
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1    
    return book