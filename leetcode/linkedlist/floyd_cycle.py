"""
Leetcode 287 : Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

Intuition : We can map the problem to a linked list problem where each value in the array points to another index.
            The duplicate in the cycle can be found using Floyd's cycle finding algorithm

            Using fast and slow pointers, find the meeting point.
            Reset the slow pointer to the head of the list, keep the fast pointer at the meeting point.
            Move both pointers one step at a time. The node where they meet again is the start of the cycle.
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # points to indexes
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # reset slow pointer to head
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow