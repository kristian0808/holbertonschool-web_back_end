#!/usr/bin/env python3
"""Returns the square value of the int or float"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns the square value of the int or float"""
    return [(i, len(i)) for i in lst]
