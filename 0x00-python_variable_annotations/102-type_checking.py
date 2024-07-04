#!/usr/bin/env python3
'''Type checking
'''
from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Create a list with each element in the tuple `lst` repeated `factor` times.

    Args:
        lst (Tuple[int, ...]): A tuple of integers.
        factor (int): The number of times to repeat each element (default is 2).

    Returns:
        List[int]: A list with repeated elements.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


# Define a tuple of integers
array = (12, 72, 91)

# Zoom array with default factor (2)
zoom_2x = zoom_array(array)

# Zoom array with a factor of 3
zoom_3x = zoom_array(array, 3)

if __name__ == "__main__":
    # Print the function's type annotations
    print(zoom_array.__annotations__)

