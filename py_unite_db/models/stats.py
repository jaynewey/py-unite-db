from typing import Any

from .base_model import BaseModel


class Stats(BaseModel):
    """Stats of a pokemon at a particular level

    View all stats [here](https://unite-db.com/stats) on the unite-db website.
    """

    # absolute
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    # percentages
    crit: int
    cooldown_reduction: int
    lifesteal: int

    @staticmethod
    def _transform(v: dict[str, Any]) -> dict[str, Any]:
        v["cooldown_reduction"] = v.pop("cdr")  # make cdr more user friendly
        return v
