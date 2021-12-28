from functools import cached_property

from .api_base import ApiBase, endpoint
from .models import BattleItem, HeldItem, Pokemon


class UniteDbBase(ApiBase):
    """
    All attributes fetched from the API are cached by default.

    For example, given a instance of this object `unite_db`, you can explicitly delete
    the cache of pokemon by doing:

    ```python
    del unite_db.pokemon
    ```

    And on the next

    ```python
    unite_db.pokemon
    ```

    The value will be pulled freshly from the API.

    It will be very rare you need to this; the API is not updated that frequently.
    """

    def __init__(self, base_url: str, client=None):
        super().__init__(base_url, client)

    @endpoint
    def held_items(self) -> list[HeldItem]:
        """Get all held items.

        Returns list of [`HeldItem`][py_unite_db.models.HeldItem].
        """

    @endpoint
    def battle_items(self) -> list[BattleItem]:
        """Get all battle items.

        Returns list of [`BattleItem`][py_unite_db.models.BattleItem].
        """

    @cached_property
    def pokemon(self) -> list[Pokemon]:
        """Get all pokemon.

        Returns list of [`Pokemon`][py_unite_db.models.Pokemon].
        """
        # clear endpoint caches
        # NOTE: Allow separation of cached and uncached endpoints to avoid this?
        del self._pokemon
        del self._stats

        # Combine `_pokemon` and `_stats`
        # get stats by pokemon name
        stats = {stat.get("name", ""): stat["level"] for stat in self._stats.json()}
        pokemon = self._pokemon.json()
        # rename default "stats" to "stars"
        for p in pokemon:
            p["stars"] = p.pop("stats", None)
        # join pokemon and stats together, and parse as `Pokemon` model
        return [Pokemon.parse_obj(p | {"stats": stats.get(p["name"])}) for p in pokemon]

    @endpoint
    def _pokemon(self):
        """Private pokemon getter.

        Used in background by [py_unite_db.unite_db.UniteDbBase.pokemon]][]
        """

    @endpoint
    def _stats(self):
        """Private stat getter.

        Used in background by [py_unite_db.unite_db.UniteDbBase.pokemon]][]
        """
