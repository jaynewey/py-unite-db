from pathlib import Path

from py_unite_db import BASE_URL

from .mock_unite_db import MockUniteDb


def test_endpoint_cache():
    mock_unite_db = MockUniteDb()
    aeos_cookie = mock_unite_db.held_items[0]

    assert aeos_cookie.name == "Aeos Cookie"

    # now change the data at "held_items.json"

    mock_unite_db._adapter.register_uri(
        "GET",
        f"{BASE_URL}/held_items.json",
        json=MockUniteDb._load_json(
            Path(__file__).resolve().parent / "responses/held_items_2.json"
        ),
    )

    # the cached version should not change
    assert mock_unite_db.held_items[0].name == "Aeos Cookie"

    # now remove cache (forcing the refetch)
    del mock_unite_db.held_items

    # value is now new value
    assert mock_unite_db.held_items[0].name == "Assault Vest"


def test_pokemon_cache():
    mock_unite_db = MockUniteDb()

    assert mock_unite_db.pokemon[0].name == "Blastoise"
    assert mock_unite_db.pokemon[0].stats[0].hp == 3225

    # now change the data at "pokemon.json" and "stats.json"

    for endpoint in ("pokemon", "stats"):
        mock_unite_db._adapter.register_uri(
            "GET",
            f"{BASE_URL}/{endpoint}.json",
            json=MockUniteDb._load_json(
                Path(__file__).resolve().parent / f"responses/{endpoint}_2.json"
            ),
        )

    # the cached version should not change
    assert mock_unite_db.pokemon[0].name == "Blastoise"
    assert mock_unite_db.pokemon[0].stats[0].hp == 3225

    # now remove cache (forcing the refetch)
    del mock_unite_db.pokemon

    # value is now new value
    assert mock_unite_db.pokemon[0].name == "Absol"
    assert mock_unite_db.pokemon[0].stats[0].hp == 3000
