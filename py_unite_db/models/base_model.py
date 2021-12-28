from typing import Any, Type

from pydantic import BaseModel as PydanticBaseModel
from pydantic import root_validator


class BaseModel(PydanticBaseModel):
    """Globally configured Pydantic base model used by api wrapper."""

    class Config:
        frozen = True  # Disable mutation of attributes and make hashable

    @root_validator(pre=True)
    def _flatten_tags(cls: Type["BaseModel"], v: dict[str, Any]) -> dict[str, Any]:
        return cls._transform(v)

    @staticmethod
    def _transform(v: dict[str, Any]) -> dict[str, Any]:
        """Override if need to transform the json response before unpacking

        By default doesn't transform anything.
        """
        return v
