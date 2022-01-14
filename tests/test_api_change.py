import pytest
from pydantic.error_wrappers import ValidationError

from py_unite_db import UniteDb

unite_db = UniteDb()


@pytest.mark.webtest
def test_pokemon_change():
    try:
        unite_db.pokemon
    except ValidationError as e:
        pytest.fail(e)


@pytest.mark.webtest
def test_held_items_change():
    try:
        unite_db.held_items
    except ValidationError as e:
        pytest.fail(e)


@pytest.mark.webtest
def test_battle_items_change():
    try:
        unite_db.battle_items
    except ValidationError as e:
        pytest.fail(e)
