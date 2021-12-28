import json
from pathlib import Path
from typing import Any, Union

import requests
import requests_mock

from py_unite_db import BASE_URL, UniteDbBase


class MockUniteDb(UniteDbBase):
    """
    Mock UniteDb client. Routes all requests through mock adapter to load json from
    snapshots dir.
    """

    _adapter: requests_mock.Adapter

    def __init__(self):
        session = requests.Session()
        self._adapter = requests_mock.Adapter()
        session.mount("https://", self._adapter)

        for name in self._get_endpoints():
            self._register_endpoint(f"{name.lstrip('_')}.json")

        super().__init__(BASE_URL, client=session)

    @staticmethod
    def _load_json(path: Path) -> Union[list[Any], dict[str, Any]]:
        with open(path, "r") as f:
            return json.load(f)

    def _register_endpoint(self, endpoint: str):
        response_path = Path(__file__).resolve().parent / f"responses/{endpoint}"

        self._adapter.register_uri(
            "GET",
            f"{BASE_URL}/{endpoint}",
            json=self._load_json(response_path) if response_path.exists() else {},
        )
