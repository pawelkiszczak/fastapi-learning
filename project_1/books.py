from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Fiction"},
    {"title": "Title Two", "author": "Author Two", "category": "Fiction"},
    {"title": "Title Three", "author": "Author Three", "category": "Fiction"},
    {"title": "Title Four", "author": "Author Four", "category": "Non-Fiction"},
    {"title": "Title Five", "author": "Author Five", "category": "Non-Fiction"},
    {"title": "Title Six", "author": "Author Two", "category": "Non-Fiction"},
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
        if (
            book["author"].casefold() == book_author.casefold()
            and book["category"].casefold() == category.casefold()
        ):
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == updated_book["title"].casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


@app.get("/books/by_author/{author}")
async def read_books_by_query_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if author.casefold() == book["author"].casefold():
            books_to_return.append(book)

    return books_to_return
