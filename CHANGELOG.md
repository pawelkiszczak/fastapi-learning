# Changelog

All notable changes to this project are recorded here. This file shows the differences
between the current version and the previous release. The current release is treated
as the initial public state.

## [0.1.1] - 2025-12-10

- Bumped version from `0.1.0` to `0.1.1`.
- Added initial FastAPI app (`books.py`) with two endpoints:
  - `GET /api-endpoint` — returns `{"message": "Hello, World!"}` (simple health/example).
  - `GET /books` — returns an in-memory `BOOKS` list of 5 books (fields: `title`, `author`, `category`).
- Added `CHANGELOG.md`.
- Dependencies (from `pyproject.toml`): `fastapi`, `uvicorn`.

### Notes

- Treat `0.1.1` as the initial release for this repository; subsequent changes should be
  recorded as additional versioned sections here.

## [0.1.2] - 2025-12-10

- Commit: `ffb7ab21` — `update endpoint with dynamic parameter`
- Files changed: `books.py`

### Summary

- Added `GET /books/{book_title}` to fetch a single book by title (case-insensitive match).

### Details

- The endpoint returns the matching book object when found, otherwise returns `{"message": "Book not found"}`.
- Renamed the handler to `read_book_by_title` to avoid a duplicate function name with `read_all_books`.

### Notes

- Move this section under an `Unreleased` header only if you plan additional changes before releasing.

## [0.1.3] - 2025-12-10

- **Commits:**
  - `e6de0ba6` — `query strings and paths`
  - `a47e7ed4` — `DELETE & testing endpoint`
- **Date:** 2025-12-10
- **Files changed:** `books.py`, `pyproject.toml`

### Summary

- Added query-string and path-based endpoints to filter books by `category` and by `author` + `category`.
- Added `POST`, `PUT`, and `DELETE` endpoints for managing the in-memory `BOOKS` collection; added `Title Six` to the dataset.

### Details

- `GET /books/` accepts a query parameter `category` and returns books matching the category (case-insensitive).
- `GET /books/{book_author}/` accepts path parameter `book_author` and query parameter `category`; returns books matching both author and category (case-insensitive).
- `POST /books/create_book` accepts a request body and appends a new book to `BOOKS`.
- `PUT /books/update_book` accepts a request body and replaces an existing book (matched by `title`) with the provided data.
- `DELETE /books/delete_book/{book_title}` deletes a book matched by `title` from `BOOKS`.
- `GET /books/by_author/{author}` returns books for a given author.
- `pyproject.toml` was modified (metadata/version changes).

### Notes

- Consider adding response models and input validation for request bodies and query parameters; consider returning appropriate HTTP status codes (e.g., `201` on create, `404` when updates/deletes target non-existent resources).
