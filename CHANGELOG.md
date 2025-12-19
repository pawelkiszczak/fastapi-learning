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

## [0.1.5] - 2025-12-19

- **Commits (most recent first):**
  - `e1127e9` — `include phone_number in user creation & change number endpoint`
  - `aba36bf` — `add downgrade to alembic`
  - `d232562` — `fix alembic`
  - `7465781` — `add basic alembic`
  - `cfc1430` — `add user password change`
  - `143c29e` — `add admin route`
  - `963e043` — `update user dependency in all endpoints`
  - `f63a78e` — `add todo as verified user`
  - `b4b4f04` — `add prefixes, tags and cleanup auth.py`
  - `972056b` — `jwt decoding`
  - `f4a47b7` — `use JWT token`
  - `f7c42b2` — `user creation`
  - `fb7440a` — `add user creation`
  - `0e3dfd8` — `small rebuild and cleanup & routers added`
  - `afa3f65` — `add request validation schema and delete endpoint`
  - `a2422f7` — `add new CRUD endpoints for todos`
  - `870ead6` — `dependency injection`

### Summary

- Added user management features (user creation, password changes, phone number support, admin route).
- Introduced JWT-based authentication and updated dependency usage across endpoints.
- Added Alembic migrations and downgrade support for database schema management.
- Added or improved todos CRUD, request validation schemas, and router organization.

### Details

- `include phone_number in user creation & change number endpoint` — user schema extended to include `phone_number` and endpoints updated to accept/change it.
- `add basic alembic` / `fix alembic` / `add downgrade to alembic` — Alembic scaffolding and migrations added; downgrade support implemented.
- Authentication: JWT encoding/decoding added; `auth.py` cleaned up; endpoints now use JWT token dependency and improved guards for verified users.
- Todos: new CRUD endpoints, request schema validation, and a verified-user requirement for some operations.
- Router and project structure: small rebuild, added routers and updated dependency injection to streamline endpoints.

### Notes

- These changes reflect development activity through 2025-12-19 and should be reviewed before tagging a formal release.

## Unreleased

- No unreleased changes at this time.
