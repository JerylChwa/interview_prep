"""
Binary search can be used to improve efficiency in cases where we have to do a linear search.
They can be applied in a huge range of problems that sometimes might not be so obvious even though the concept of binary search is relatively trivial.
We will explore how to use binary search as well as explore how to use python's bisect module to help ease the use of binary search when needed.
"""

import bisect 
import random
from typing import List

"""
Leetcode 35 : Search Insert Position
Intuition : Binary search over sorted array with no duplicate values
Concerns : What kind of binary search will work / fail on a sorted array with duplicate values?
"""
class Leetcode35:
    def __init__(self, nums : List[int], target: int):
        self.nums = nums
        self.target = target
    
    """
    This only works for a strictly increasing array, if there are duplicates, and we want to find the most left occurence of target,
    this fails to find the first occurence of the target element
    """
    def handleDistinct(self):
        l = 0
        r = len(self.nums) - 1
        res = 0
        while l <= r:
            m = l + (r-l) // 2
            if self.target == self.nums[m]:
                return m
            elif self.target < self.nums[m]: # insert position at most m 
                res = m
                r = m - 1
            else: # insert position at least m + 1
                res = m + 1
                l = m + 1
        
        return res
    
    """
    This handles duplicates by just not returning immediately if we find a result
    """
    def handleDuplicate(self):
        l = 0
        r = len(self.nums) - 1
        res = 0
        while l <= r:
            m = l + (r-l) // 2
            if self.target <= self.nums[m]: # insert position at most m 
                res = m
                r = m - 1
            else: # insert position at least m + 1
                res = m + 1
                l = m + 1
        
        return res        

    """
    Python's built in bisect module handles duplicates, finds the most left / right position without breaking order
    """
    def bisectHandleDuplicate(self):
        res = bisect.bisect_left(self.nums, self.target)
        return res

def test_detect_duplicate():
    # this fails
    template = Leetcode35([1,2,3,3,3,4,5], 3)
    assert template.handleDistinct() != 2
def test_handle_duplicate():
    template  = Leetcode35([1,2,3,3,3,4,5], 3)
    assert template.handleDuplicate() == 2
def test_bisect_handle_duplicate():
    template  = Leetcode35([1,2,3,3,3,4,5], 3)
    assert template.bisectHandleDuplicate() == 2

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
            # avoids overflow
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

