#!/usr/bin/env python3
"""
Task 101 module.
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Return the value for `key` in `dct` if `key` exists, otherwise return `default`.

    Args:
        dct (Mapping[Any, T]): A dictionary or mapping of keys to values.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None]): The default value to return if `key` is not found (default is None).

    Returns:
        Union[Any, T]: The value associated with `key` if it exists, otherwise `default`.
    """
    if key in dct:
        return dct[key]
    else:
        return default
