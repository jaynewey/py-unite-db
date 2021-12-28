from pydantic import Field

from ..types import Tier
from .base_model import BaseModel


class Item(BaseModel):
    """Parent class for Battle and Held items.

    See [here](https://unite-db.com/items) for a list of all items on
    the unite-db website.
    """

    name: str = Field(..., description="Name of this item.")
    display_name: str = Field(..., description="Display name of this item.")
    tier: Tier = Field(..., description="What tier unite-db consider this item to be.")
    description: str = Field(..., description="Description of this item.")
