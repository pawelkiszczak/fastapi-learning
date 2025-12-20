try:
    from . import project_3

    __all__ = ["project_3"]
except Exception:
    # Avoid import-time errors when running tests or when the package
    # is not being imported as a proper parent package.
    __all__ = []
