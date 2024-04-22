#!/usr/bin/env python3

"""This module contains the wait_n function."""


import asyncio
from typing import List

from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: float) -> List[float]:
    """Executes wait_random n times with the specified max_delay."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
