from typing import Any, Optional

from pydantic import Field

from ..types import DamageType, Difficulty, Range, Role, Tier
from ..utils import _flatten
from .base_model import BaseModel
from .stats import Stats

POKEMON_MIN_LEVEL = 1
POKEMON_MAX_LEVEL = 15


class Evolution(BaseModel):
    name: str
    level: int


class Stars(BaseModel):
    combat: int
    resistance: int
    mobility: int
    scoring: int
    assistance: int
    total: int


class Pokemon(BaseModel):
    """Class representing a Pokemon.

    See all Pokemon [here](https://unite-db.com) on the unite-db website.

    Get all pokemon from the API using
    [`UniteDb.pokemon`][py_unite_db.UniteDb].

    Example:
        >>> from py_unite_db import UniteDb
        >>> unite_db = UniteDb()

        >>> unite_db.pokemon[0].name
        'Absol'
        >>> unite_db.pokemon[0].tier
        'C'
    """

    name: str = Field(..., description="Name of the Pokemon.")
    notes: str = Field("", description="Things to note about the Pokemon.")
    tier: Tier = Field(
        ...,
        description="""What tier unite-db consider this Pokemon to be.
    From S being the top tier, to D being the lowest.
    T is for Pokemon coming soon.""",
    )
    damage_type: DamageType = Field(..., description="Physical or special attacker.")
    stars: Optional[Stars] = Field(
        ..., description="How many stars the pokemon has for each stat in the game."
    )
    stats: list[Stats] = Field([], description="This Pokemon's stats.")
    range: Range = Field(..., description="Ranged or Melee attacker.")
    difficulty: Difficulty = Field(
        ..., description="The in-game difficulty rating of the Pokemon."
    )
    role: Role = Field(..., description="The role of the Pokemon.")
    soon: bool = Field(..., description="Whether the Pokemon is coming soon or not.")
    evolution: list[Evolution] = Field(
        [], description="List of the Pokemon's evolutions."
    )

    def stats_at(self, level: int) -> Stats:
        """Gets stats at a given level between 1 and 15.

        Args:
            level: The level at which to get stats at.

        Example:
            >>> from py_unite_db import UniteDb
            >>> UniteDb().pokemon[0].stats_at(7)
            Stats(hp=3823, attack=293, defense=109, sp_attack=47, sp_defense=76, crit=5, cooldown_reduction=10, lifesteal=0)


        If the level given is less than 1, gets level 1.
        If the level given is more than 15, gets level 15.
        """  # noqa: E501
        level = min(POKEMON_MAX_LEVEL, max(POKEMON_MIN_LEVEL, level))
        return self.stats[level - 1]

    def name_at(self, level: int) -> str:
        """Gets the name of the pokemon at a given level.

        This is only really useful if the Pokemon has evolutions.
        For example, Blastoise only becomes Blastoise at level 9.

        Example:
            >>> from py_unite_db import UniteDb
            >>> UniteDb().pokemon[1].name
            'Blastoise'
            >>> UniteDb().pokemon[1].name_at(1)
            'Squirtle'
            >>> UniteDb().pokemon[1].name_at(5)
            'Wartortle'
            >>> UniteDb().pokemon[1].name_at(9)
            'Blastoise'

        If the level given is less than 1, gets level 1.
        If the level given is more than 15, gets level 15.
        """
        # if no evolutions or level is larger than or equal to final
        if not self.evolution or level >= self.evolution[-1].level:
            return self.name
        # if more than one evolution and middle stage
        elif level >= self.evolution[0].level:
            return self.evolution[-1].name
        # if one evolution or base stage
        return self.evolution[0].name

    @staticmethod
    def _transform(v: dict[str, Any]) -> dict[str, Any]:
        return _flatten(v, "tags")
