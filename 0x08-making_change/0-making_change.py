#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    the given total
    """
    if total <= 0:
        return 0
    tem = total
    count = 0
    i = 0
    sortcoin = sorted(coins, reverse=True)
    l = len(coins)
    while tem > 0:
        if i >= n:
            return -1
        if tem - sortcoin[i] >= 0:
            rem -= sortcoin[i]
            count += 1
        else:
            i += 1
    return count
