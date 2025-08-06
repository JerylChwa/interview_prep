"""
Leetcode 287 : Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

Intuition : Choose a random number, x between 1 and n.
            Iterate through the entire array and count the number of elements <= x.
            If the count is greater than x itself, this tell us that there are duplicates.
            So now we search the left half of the search space.
            If count is less than or equal, we will just search the right half of the search space.

Note : This solves it in O(nlogn), there is a more efficient linked list solution using Floyd's cycle
"""
from typing import List 

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        res = 0
        while l <= r:
            m = l + (r-l) // 2
            cnt = 0
            for num in nums:
                if num <= m:
                    cnt += 1
            
            if cnt > m: # search left half of search space
                r = m - 1
                res = m
            else:
                l = m + 1
        
        return res


