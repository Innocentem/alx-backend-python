#!/usr/bin/env python3
"""
Task 10's module.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of the sequence `lst` if it is not empty.

    Args:
        lst (Sequence[Any]): A sequence of elements.

    Returns:
        Union[Any, None]: The first element if `lst` is not empty, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
