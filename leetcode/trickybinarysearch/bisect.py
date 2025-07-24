"""
Binary search can be used to improve efficiency in cases where we have to do a linear search.
They can be applied in a huge range of problems that sometimes might not be so obvious even though the concept of binary search is relatively trivial.
We will explore how to use binary search as well as explore how to use python's bisect module to help ease the use of binary search when needed.
"""

import bisect 
import random
from typing import List


"""
Leetcode 528 : Random Pick With Weight
Intuition : Build prefix sum of the weights and binary search over prefix sum
"""

class Leetcode528:
    def __init__(self, w : List[int]):
        self.weights = w
        self.prefix = []
        # building prefix list
        cur = 0
        for weight in self.weights:
            cur += weight
            self.prefix.append(weight)
        # keep track of total weights
        self.sum = cur

    """
    Using binary search fundamentals
    """
    def pickIndexBinarySearch(self) -> int:
        random_weight = random.randint(1, self.sum)
        l = 0
        r = len(self.prefix) - 1

        while l <= r:
            m = l + (r - l) // 2
            if random_weight <= self.prefix[m]:
                # update result
                res = m
                # continue searching left
                r = m - 1
            else:
                # search right
                l = m + 1

        return res

    """
    Using python's bisect module
    """
    def pickIndexBisect(self) -> int:
        random_weight = random.randint(1, self.sum)

        # Finds leftmost index where random_weight can be inserted to keep self.prefix sorted
        res = bisect.bisect_left(self.prefix, random_weight)

        return res
