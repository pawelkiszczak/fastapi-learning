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

## Unreleased

- **Commit:** `e6de0ba6` — `query strings and paths`
- **Date:** 2025-12-10
- **Files changed:** `books.py`, `pyproject.toml`

### Summary

- Added query-string and path-based endpoints to filter books by `category` and by `author` + `category`.
- Added an extra book entry (`Title Six`) to the in-memory `BOOKS` list.

### Details

- `GET /books/` now accepts a query parameter `category` and returns books matching the category (case-insensitive).
- `GET /books/{book_author}/` accepts path parameter `book_author` and query parameter `category`; returns books matching both author and category (case-insensitive).
- `pyproject.toml` was modified (likely a version bump or metadata change).

### Notes

- Consider adding response models and input validation for query parameters; also consider returning `404` when no results are found for single-book queries.
