"""
Leetcode 162 : Find peak element

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

nums[i] != nums[i + 1] for all valid i.

Concerns : 
Trivial to do in O(n) time by just traversing the entire array.
Binary search intuition is not so obvious.
"""
from typing import List

class Leetcode162():
    """
    Intuition : 
    Notice these facts:
    1. We can return ANY of the peaks
    2. Any element outside the array is negative infinity.
    3. There are no consecutive duplicate elements -> A valid peak is guaranteed to be found

    We initialise the binary search and now we are at the middle element.
    For ease of discussion, M : middle value, L : left neighbor value, R : right neighbor value
    There are 3 different cases.
    Case 1 : M > L and M > R, we found valid peak M
    
    Case 2 : M < L (if R just swap),
    On the LHS, IF the array is monotonically decreasing, there is no peak value.
    Of course, if the array is NOT monotonically decreasing, there will be a peak value but this is not guaranteed.

    On the RHS, since L is already greater than M,
    Case 1 : The RHS array is motonically increasing, peak value will then be the last value since its more than the element outside the array
    Case 2 : The RHS array is NOT monotonically increasing, a peak value is still guaranteed to be located in the RHS.
    
    This leads us to the conclusion that we just have to search the side with an element higher than M.
    """
    def findpeak(self, nums : List[int]) -> int:
        length = len(nums)

        # defining the binary search space
        l = 0 
        r = length - 1
        # start binary search
        while l <= r:
            m = l + (r - l) // 2 # prevents integer overflow if instead (l + r) // 2
            
            middle = nums[m]
            left = nums[m-1] if m - 1 >= 0 else float("-inf")
            right = nums[m+1] if m + 1 < length else float("-inf")
            print(f"m : {m}")
            print(f"middle : {middle}")
            print(f"left : {left}")
            print(f"right : {right}")
            
            # found peak
            if middle > left and middle > right: 
                return m 
            elif middle < right: # search rhs
                l = m + 1
            else: # search lhs
                r = m - 1
    

def test_one():
    sol = Leetcode162()
    assert sol.findpeak([1,2,3,1]) == 2
def test_two():
    sol = Leetcode162()
    assert sol.findpeak([1,2,1,3,5,6,4]) == 5




        