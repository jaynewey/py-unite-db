from typing import Any

from pydantic import Field

from .item import Item


class BattleItem(Item):
    """Class representing a Battle Item.

    Get all battle items from the api with
    [`UniteDb.battle_items`][py_unite_db.UniteDb].

    In the game, you can select one battle item per battle.
    """

    cooldown: int = Field(..., description="The cooldown of the item in seconds.")
    unlock_level: int = Field(
        ..., description="The trainer level at which this item is unlocked."
    )

    @staticmethod
    def _transform(v: dict[str, Any]) -> dict[str, Any]:
        v["unlock_level"] = v.pop("level")
        return v
