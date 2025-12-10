from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Fiction"},
    {"title": "Title Two", "author": "Author Two", "category": "Fiction"},
    {"title": "Title Three", "author": "Author Three", "category": "Fiction"},
    {"title": "Title Four", "author": "Author Four", "category": "Non-Fiction"},
    {"title": "Title Five", "author": "Author Five", "category": "Non-Fiction"},
    {"title": "Title Six", "author": "Author Two", "category": "Non-Fiction"}
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

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book["category"].casefold() == category.casefold():
            books_to_return.append(book)
    
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (book["author"].casefold() == book_author.casefold() and \
            book["category"].casefold() == category.casefold()):
            books_to_return.append(book)
    
    return books_to_return