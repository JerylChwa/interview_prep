"""
Leetcode 221
"""

from typing import List 

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        dp = [0 for _ in range(COLS)] 
        largest_length = 0
        prev = dp
        for r in range(ROWS):
            new_dp = [0]*(COLS)
            for c in range(COLS):                
                if matrix[r][c] == "1":                    
                    left = int(new_dp[c-1]) if c - 1 >= 0 else 0 
                    top = prev[c] 
                    diagonal = prev[c-1] if c-1 >= 0 else 0
                    new_dp[c] = min(left, top, diagonal) + int(matrix[r][c])                    
                    largest_length = max(largest_length, new_dp[c])
            prev = new_dp

        return largest_length*largest_length