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
