# My Rating = 2
# https://leetcode.com/contest/weekly-contest-219/problems/count-of-matches-in-tournament/

import math
class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n!=1:
            count += int(math.floor(n/2))
            n=int(math.ceil(n/2))
        return count