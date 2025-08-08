from typing import List

class Solution:
    """
    Don't have to store whose turn it is in the cache as for each unique l, r, if the interval is even its guaranteed to be Alice turn
    Can measure whose turn based on the length so no need to manually flip the flag as well
    """
    def stoneGame(self, piles: List[int]) -> bool:
                
        # do a dfs on the interval space of piles
        # alternate turns between alice and bob
        # if alice turn, then add to her sum
        # dfs will return the max sum of alice within a said interval of piles
        # interval range will be inclusive
        mem = {}

        def dfs(l, r, add):
            if (l,r) in mem:
                return mem[(l,r)]
            if l > r:
                return 0

            
            # recurise call logic
            # if add == true, we will add value of the side we choose
            # if add == false, we do not add and continue
            # and of course we have to alternate the turns after we are done
            left = piles[l] if add else 0
            right = piles[r] if add else 0
            mem[(l, r)] = max(left + dfs(l+1, r, not add), 
                       right + dfs(l, r-1, not add))
            return mem[(l,r)]

        return dfs(0, len(piles)-1, True) > sum(piles) // 2
        


# def test_stones():
#     sol = Solution()
#     assert sol.stoneGame([5,3,4,5]) == True







sol = Solution()
print(sol.stoneGame([7,7,12,16,41,48,41,48,11,9,34,2,44,30,27,12,11,39,31,8,23,11,47,25,15,23,4,17,11,50,16,50,38,34,48,27,16,24,22,48,50,10,26,27,9,43,13,42,46,24]))

# print(sol.stoneGame([5,3,4,5]))


# call = [0]
# def dfs():
#     print(f"enter call {call[0]}")
#     call[0] += 1
#     if call[0] < 3:
#         dfs()
#     call[0] -= 1
#     print(f"exit call {call[0]}")

# dfs()