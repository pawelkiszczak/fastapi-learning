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
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)


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

@app.post("/create_book")
async def create_book(book_request: BookRequest) -> None:
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)
    
    
def find_book_id(book: Book) -> Book:
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1    
    return book