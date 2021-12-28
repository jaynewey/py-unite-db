from .mock_unite_db import MockUniteDb

eject_button = MockUniteDb().battle_items[0]


def test_attributes():
    assert eject_button.name == "Eject Button"
    assert eject_button.display_name == "Eject Button"
    assert eject_button.description == "Quickly move in a designated direction."
    assert eject_button.tier == "S"
    assert eject_button.cooldown == 70
    assert eject_button.unlock_level == 11
