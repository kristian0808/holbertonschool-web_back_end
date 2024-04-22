#!/usr/bin/env python3
"""Sums a list of floats and integers"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a list of floats"""
    return sum(mxd_lst)
