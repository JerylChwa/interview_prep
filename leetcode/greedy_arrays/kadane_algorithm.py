"""
Kadane's algorithm 

Classic Problem: Maximum Subarray Sum

Given an integer array nums, find the subarray with the largest sum, and return its sum
"""
from typing import List

class KadaneAlgorithm():
    """
    Main idea is to traverse over the array from left to right,
    and for each element, find the maximum sum among all subarrays ending at that element.
    The result is the maximum of all these values.

    At any element, we have 2 choices

    Choice 1: 
    Extend the maximum subarray ending at the previous element by adding the current element to it.
    If the maximum subarray ending at the previous index is positive, it is always better to extend the subarray.

    Choice 2:
    Start a new subarray starting from the current element. 
    If the maximum subarray sum ending at the previous index is negative, it is always better to start a new subarray from the current element.
    """


    def maxSubArray1(self, nums: List[int]) -> int:
        
        # Stores the result (maximum sum found so far)
        res = nums[0]

        # Maximum sum of subarray
        maxEnding = nums[0] 

        # start from index 1 since index 0 has already been computed
        for i in range(1, len(nums)):

            # Either extend the previous subarray or start new from current element
            maxEnding = max(maxEnding + nums[i], nums[i])

            # Update result if new subarray sum is larger
            res = max(res, maxEnding)
        
        return res
    
    
    
    def maxSubArray2(self, nums: List[int]) -> int:

        res = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0
            total += n
            res = max(res, total)
        
        return res

    def test(self):
        print(self.maxSubArray2([-3, -1, -2]) == -1)

x = KadaneAlgorithm()
x.test()

