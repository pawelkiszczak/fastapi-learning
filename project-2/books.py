from fastapi import FastAPI, Body

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
async def create_book(new_book=Body()) -> None:
    BOOKS.append(new_book)