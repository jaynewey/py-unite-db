from typing import Any, Callable


def _flatten(d: dict[str, Any], *keys: str) -> dict[str, Any]:
    """Pulls up values from nested dict into outer dict.

    The keys are evaluated in the order they are provided to the function.
    Pulled up values replace those that already exist in the outer dict.
    The key original key provided will be removed unless it is pulled up from the
    nested dict.

    Example:
        >>> flatten({"a": "b", "c": {"c": "d"}}, "c")
        {"a": "b", "c": "d"}
    """
    for key in keys:
        if isinstance(d.get(key), dict):
            d |= d.pop(key)
    return d


def _squash(
    d: dict[str, Any], new_key: str, cond: Callable[[str], bool]
) -> dict[str, Any]:
    """Squash all keys that match the given condition into a list of their values."""
    values = [v for k, v in d.items() if cond(k)]
    return {k: v for k, v in d.items() if not cond(k)} | {new_key: values}


def _percent_as_float(percent: str) -> float:
    """Converts a percentage formatted string to float

    If it is not a percentage, just cast to float.

    Args:
        percent: the percentage formatted string to convert
    """
    return float(percent.rstrip("%")) / 100 if percent.endswith("%") else float(percent)


def _pretty_float(num: float) -> str:
    """Converts a float to a string.

    If the float is equal to its integer representation, don't keep the trailing 0.
    """
    return str(int(num) if int(num) == num else num)


def _index_by(list_: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    """Takes list of `dict`s and indexes by a key rather than list index.

    If the key is not in the inner `dict`, it is ignored.
    """
    return {d[key]: d for d in list_ if key in d.keys()}
