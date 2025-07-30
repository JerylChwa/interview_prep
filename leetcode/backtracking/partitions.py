"""
Leetcode 131 : Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s

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
        res = []
        
        def ispalin(word: str):
            return word == word[::-1]
        
        # r represents remaining string left
        def dfs(r: str, path: List[str]):
            if not r:
                res.append(path)
                return 
            # choosing a prefix
            for i in range(1, 1+len(r)):
                prefix = r[:i]
                postfix = r[i:]
                if ispalin(prefix): #continue searching other prefixes
                    dfs(postfix, path+[prefix])
        
        dfs(s, [])
        return res