"""
Leetcode 131 : Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s
A palindrome is a word, phrase, number, or other sequence of characters that reads the same backward as forward

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
"""

from typing import List

class Leetcode131:
    """
    Essentially backtracking on the different ways to chop up the prefix of the array,
    while ensuring that the prefix is a valid palindrome.
    We reach the base case when there is no more of the array left which means that all that we have added in our path are valid palindromes.
    We can add this combination of palindromes to our result
    """

    def partition(self, s: str) -> List[List[str]]:
        res : List[str] = []
        curr : List[List[str]] = []
        def ispalin(start : int, end : int) -> bool:
            while start < end:
                if s[start] != s[end]:
                    return False 
                start += 1
                end -= 1            
            return True 
            
        def dfs(index : int):
            if index >= len(s):
                res.append(curr[:])
                return 
            
            for end in range(index, 1+len(s)):
                if ispalin(index, end): #continue searching other prefixes
                    curr.append(s[index:end+1])
                    dfs(end+1)
                    curr.pop()
        
        dfs(0)
        return res