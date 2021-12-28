from .mock_unite_db import MockUniteDb

mock_unite_db = MockUniteDb()


def test_name():
    assert mock_unite_db.pokemon[0].name == "Absol"


def test_stats():
    # using indexes
    assert mock_unite_db.pokemon[0].stats[0].hp == 3000
    assert mock_unite_db.pokemon[0].stats[14].hp == 6000

    # using `stats_at` method
    assert mock_unite_db.pokemon[0].stats_at(1).hp == 3000
    assert mock_unite_db.pokemon[0].stats_at(15).hp == 6000
    # test round up/down
    assert mock_unite_db.pokemon[0].stats_at(0).hp == 3000
    assert mock_unite_db.pokemon[0].stats_at(16).hp == 6000


def test_stars():
    assert mock_unite_db.pokemon[0].stars.combat == 7
