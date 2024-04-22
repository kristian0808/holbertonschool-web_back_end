#!/usr/bin/env python3
"""Returns the square value of the int or float"""

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """Returns the square value of the int or float"""
    return (k, v * v)
