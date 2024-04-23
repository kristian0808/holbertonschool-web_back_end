#!/usr/bin/env python3
"""This module contains the async_comprehension coroutine."""

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def async_comprehension():
    """Yield a list of 10 random numbers between 0 and 10."""
    return [await async_generator() for _ in range(10)]
