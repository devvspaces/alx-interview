#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.

    :param coins: a list of the values of the coins in your possession
    :type coins: list
    :param total: the total amount of money to make change for
    :type total: int
    :return: the fewest number of coins needed to meet the total
    :rtype: int
    """
    if total <= 0:
        return 0
    remainder = total
    count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remainder > 0:
        if coin_index >= n:
            return -1
        if remainder - sorted_coins[coin_index] >= 0:
            remainder -= sorted_coins[coin_index]
            count += 1
        else:
            coin_index += 1
    return count
