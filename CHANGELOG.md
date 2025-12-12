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

## [0.1.4] - 2025-12-10

- **Commit:** `ed020b2c` — `add more PUT & DELETE`
- **Date:** 2025-12-10
- **Files changed:** `project-2/books.py`

### Summary

- Continued improvements to CRUD endpoints: added more `PUT`/`DELETE` functionality and tests in the `project-2` example.

### Details

- Enhanced PUT/DELETE handling in `project-2/books.py` (see commit `ed020b2c`).
- Small refactors and test scaffolding for the `project-2` example.

### Notes

- Consider adding validation and proper HTTP status responses for create/update/delete operations (e.g., `201` on create, `204` on successful delete, `404` when not found).

## Unreleased

- **Commits (most recent first):**
  - `2e1096e` — `update makefile & rename dirs`
  - `b28ad70` — `rename dirs and update makefile`
  - `c26c186` — `add http exceptions`
  - `56eed13` — `add Makefile`
  - `179a438` — `add query & path validation`

### Summary

- Project structure renamed (directories) and Makefile improved to support `uv run` usage and configurable `APP_NAME`.
- Added HTTP exception handling to endpoints to return proper status codes for error cases.
- Validation added for query/path parameters in some endpoints.

### Details

- `update makefile & rename dirs` / `rename dirs and update makefile` — Makefile targets and examples updated; callers can run apps with `make run APP_NAME=module:app` and lint/format with `make lint FILES=...`.
- `add http exceptions` — endpoints updated to raise HTTP exceptions on invalid input or not-found cases (see `project_*/books.py`).
- `add Makefile` — initial Makefile added (subsequently refined).
- `add query & path validation` — added basic validation for query and path parameters in book endpoints.

### Notes

- These changes are kept as `Unreleased` (not a release). When ready, promote this section to a versioned release (e.g., `[0.1.5] - YYYY-MM-DD`) and tag accordingly.
