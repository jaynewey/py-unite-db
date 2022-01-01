# py-unite-db

> Unnofficial Python wrapper for the unite-db.com REST API.

## Introduction

Please be warned that this is an unofficial wrapper and the REST API is a private one, so please do not abuse it.

If you are publishing any of the data collected with this API, please give credit to [`unite-db`](https://unite-db.com/). They spend many hours collecting this data.

### Installation

The package is installable via `pip`.

```sh
pip install py-unite-db
```

### Usage

Import the [`UniteDb`][py_unite_db.UniteDb] object:

```python
from py_unite_db import UniteDb

unite_db = UniteDb()
```

Let's get the names of all supporter Pokemon:

```python
>>> [pokemon.name for pokemon in unite_db.pokemon if pokemon.role == "Supporter"]
['Blissey', 'Eldegoss', 'Mr.Mime', 'Wigglytuff']
```

### What can I fetch?

See what you can fetch with the [`UniteDb`][py_unite_db.UniteDb] object.

To see what attributes belong to each model, have a look at the [models][py_unite_db.models.Pokemon].
