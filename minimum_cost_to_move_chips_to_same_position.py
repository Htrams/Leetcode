# My Rating = 2
# https://leetcode.com/explore/featured/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3520/

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds = 0
        evens = 0
        for chip in position:
            if chip%2==0:
                evens += 1
            else:
                odds += 1
        return min(odds,evens)