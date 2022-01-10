import requests

from . import models, types
from .unite_db import UniteDbBase

__version__ = "0.2.1"

BASE_URL = "https://unite-db.com"


class UniteDb(UniteDbBase):
    """Wrapper for the Unite DB rest API.

    Example:
        >>> from py_unite_db import UniteDb
        >>> unite_db = UniteDb()
        >>> unite_db.pokemon[0].name
        'Absol'
        >>> unite_db.held_items[0].name
        'Aeos Cookie'
    """

    def __init__(self):
        super().__init__(BASE_URL, requests.Session())


__all__ = ["BASE_URL", "UniteDb", "types", "models"]
