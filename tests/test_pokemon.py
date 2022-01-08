from .mock_unite_db import MockUniteDb

mock_unite_db = MockUniteDb()


def test_name():
    assert mock_unite_db.pokemon[0].name == "Blastoise"


def test_name_at():
    assert mock_unite_db.pokemon[0].name_at(0) == "Squirtle"
    assert mock_unite_db.pokemon[0].name_at(1) == "Squirtle"

    assert mock_unite_db.pokemon[0].name_at(5) == "Wartortle"

    assert mock_unite_db.pokemon[0].name_at(9) == "Blastoise"
    assert mock_unite_db.pokemon[0].name_at(16) == "Blastoise"


def test_stats():
    # using indexes
    assert mock_unite_db.pokemon[0].stats[0].hp == 3225
    assert mock_unite_db.pokemon[0].stats[14].hp == 9800

    # using `stats_at` method
    assert mock_unite_db.pokemon[0].stats_at(1).hp == 3225
    assert mock_unite_db.pokemon[0].stats_at(15).hp == 9800
    # test round up/down
    assert mock_unite_db.pokemon[0].stats_at(0).hp == 3225
    assert mock_unite_db.pokemon[0].stats_at(16).hp == 9800


def test_stars():
    assert mock_unite_db.pokemon[0].stars.combat == 4


def test_evolutions():
    assert mock_unite_db.pokemon[0].evolution[0].name == "Squirtle"
    assert mock_unite_db.pokemon[0].evolution[1].name == "Wartortle"
