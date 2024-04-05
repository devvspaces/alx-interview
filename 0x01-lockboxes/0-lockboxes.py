#!/usr/bin/python3
'''A module for Lockboxes interview question.
'''


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.

    :param boxes: a list of lists
    :type boxes: list
    :return: True if all boxes can be opened, else False
    :rtype: bool
    """
    n = len(boxes)
    gotten = set([0])
    ungotten = set(boxes[0]).difference(set([0]))
    while len(ungotten) > 0:
        boxIdx = ungotten.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in gotten:
            ungotten = ungotten.union(boxes[boxIdx])
            gotten.add(boxIdx)
    return n == len(gotten)
