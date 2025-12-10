from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Category One"},
    {"title": "Title Two", "author": "Author Two", "category": "Category Two"},
    {"title": "Title Three", "author": "Author Three", "category": "Category Three"},
    {"title": "Title Four", "author": "Author Four", "category": "Category Four"},
    {"title": "Title Five", "author": "Author Five", "category": "Category Five"},
]

@app.get("/api-endpoint")
async def first_api_endpoint():
    return {"message": "Hello, World!"}

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book_by_title(book_title: str):
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            return book
    
    return {"message": "Book not found"}