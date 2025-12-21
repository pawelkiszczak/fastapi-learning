try:
    from . import tests, todoapp

    __all__ = ["todoapp", "tests"]
except Exception:
    # Avoid import-time errors when running tests or when the package
    # is not being imported as a proper parent package.
    __all__ = []
