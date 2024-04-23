#!/usr/bin/env python3
"""This module contains the async_comprehension coroutine."""

import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def async_comprehension() -> list:
    """Collect 10 random numbers using an async comprehension."""
    return [i async for i in async_generator()]
