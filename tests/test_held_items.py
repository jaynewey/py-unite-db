from .mock_unite_db import MockUniteDb

aeos_cookie = MockUniteDb().held_items[0]


def test_effect_at():
    assert aeos_cookie.effect.effect_at(1) == 100
    assert aeos_cookie.effect.effect_at(10) == 150
    assert aeos_cookie.effect.effect_at(20) == 200

    assert aeos_cookie.scaling_effects[0].effect_at(1) == 8
    assert aeos_cookie.scaling_effects[0].effect_at(15) == 120
    assert aeos_cookie.scaling_effects[0].effect_at(30) == 240


def test_description_at():
    assert aeos_cookie.effect.description_at(1) == "100 Max HP"
    assert aeos_cookie.scaling_effects[0].description_at(1) == "HP +8"
