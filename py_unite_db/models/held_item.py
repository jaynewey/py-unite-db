from abc import ABC, abstractmethod
from typing import Any

from ..utils import _percent_as_float, _pretty_float
from .base_model import BaseModel
from .item import Item

HELD_ITEM_MIN_LEVEL = 1
HELD_ITEM_MAX_LEVEL = 30


class ItemEffect(ABC, BaseModel):
    """Class representing the effect a held item gives."""

    label: str

    @abstractmethod
    def description_at(self, level: int) -> str:
        """Calculates the description of the item at a given level.

        Args:
            level: The item level to calculate the description at. (Between 1-30)

        Returns:
            The description at the given level. e.g `Max HP +240`
        """

    @abstractmethod
    def _effect_at(self, level: int) -> float:
        ...

    def effect_at(self, level: int) -> float:
        """Calculates the effect of the item at a given level.

        Args:
            level: The item level the calculate the effect at. (Between 1-30)

        Returns:
            The weight of effect at the given level e.g `240`
        """
        return self._effect_at(
            min(HELD_ITEM_MAX_LEVEL, max(HELD_ITEM_MIN_LEVEL, level))
        )


class LevelItemEffect(ItemEffect):
    level1: str
    level10: str
    level20: str

    def _str_effect_at(self, level: int) -> str:
        if level >= 20:
            return self.level20
        elif level >= 10:
            return self.level10
        else:
            return self.level1

    def _effect_at(self, level: int) -> float:
        return _percent_as_float(self._str_effect_at(level))

    def description_at(self, level: int) -> str:
        return f"{self._str_effect_at(level)} {self.label}"


class ScalingItemEffect(ItemEffect):
    percent: bool
    initial: int
    start: int
    skip: int
    increment: float

    def _effect_at(self, level: int) -> float:
        # ensure the level given is valid
        return self.initial + self.increment * ((level - 1) // (self.skip + 1))

    def description_at(self, level: int) -> str:
        return f"{self.label} +{_pretty_float(self.effect_at(level))}"


class HeldItem(Item):
    """Class representing a held item.

    Get all held items from the api with
    [`UniteDb.held_items`][py_unite_db.UniteDb].

    In the game, you can select up to 3 held items in battle.
    Held items can be upgraded up to level 30.
    """

    effect: LevelItemEffect
    """The effect of the held item"""
    scaling_effects: list[ScalingItemEffect]

    @staticmethod
    def _transform(v: dict[str, Any]) -> dict[str, Any]:
        v["description"] = v.pop("description1")
        v["scaling_effects"] = v.pop("stats")
        # make base for main effect
        v["effect"] = {"label": v.get("description3", "")} | {
            k: v.get(k, "") for k in ("level1", "level10", "level20")
        }
        return v
