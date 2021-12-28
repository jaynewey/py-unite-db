from abc import ABC
from functools import wraps
from typing import Any, Callable, Generic, Optional, Type, TypeVar

from uplink import Consumer, get, returns

T = TypeVar("T")


class endpoint(property, Generic[T]):
    """Decorator that automatically interfaces with ApiBase and caches return.

    It allows a restricted, but very clean syntax for defining api endpoints.

    Acts like a `property`. This decorator should only really be used inside
    `ApiBase` as it assumes a `_consumer` attribute and the relevant
    `get_` methods to be bound to the consumer.

    Example:

    ```python
    class Api(ApiBase):
        def __init__(self):
            super().__init__(base_url="https://api.com")

        @endpoint
        def colours(self) -> list[str]:
            \"\"\"Some colours to fetch at https://api.com/colours.json\"\"\"

    >>> Api().colours
    ["red", "yellow", "blue"]
    ```
    """

    _cached: Optional[T] = None

    def __init__(self, f: Callable[[Any], T]):
        @wraps(f)
        def _get(obj: ApiBase):
            """Fetches cached value if exists, else fetch from"""
            self._cached = (
                self._cached
                if self._cached is not None
                else getattr(obj._consumer, f"get_{f.__name__.lstrip('_')}")()
            )
            return self._cached

        def _del(obj: ApiBase):
            """Removes value from cache"""
            self._cached = None

        super().__init__(fget=_get, fdel=_del)


class ApiBase(ABC):
    """Finds all `endpoints` and constructs a `Consumer` which has all of the
    required `get_` methods for the endpoints.
    """

    _consumer: Consumer

    def __init__(self, base_url: str, client=None, consumer: Type[Consumer] = Consumer):
        """
        Args:
            base_url: Base url to be passed to `uplink.Consumer`
            client: Client to be passed to `uplink.Consumer`
            consumer: Comsumer subclass for the consumer to extend.
        """
        # construct meta type with all methods required by endpoints
        # instantiate, and set to `_consumer` attribute.
        self._consumer = type(
            "ConsumerMeta",
            (consumer,),
            {
                # desugared decorators on empty function
                # strip leading `_` so private functions can be used with `endpoint`
                f"get_{name.lstrip('_')}": self.__get_wrapped_method(
                    name,
                    # Make sure we tell uplink what type response we expect
                    # get this from the function type annotation
                    getattr(self.__class__, name).fget.__annotations__.get("return"),
                )
                for name in self._get_endpoints()
            },
        )(base_url, client=client)

    def __get_wrapped_method(self, name: str, rtype: Optional[type]):
        if rtype is None:
            return get(f"{name.lstrip('_')}.json")(lambda _: ...)
        else:
            return returns.json(rtype)(self.__get_wrapped_method(name, None))

    def _get_endpoints(self) -> list[str]:
        """Gets all endpoint decorator names in class and subclasses"""
        return [
            name
            for name in dir(self)
            if type(getattr(self.__class__, name, None)) == endpoint
        ]
