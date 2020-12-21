# My Rating = 3
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3559/

from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        memo = defaultdict(int)
        count = 0
        for t in time:
            temp = t%60
            if 60-temp in memo or (temp==0 and 0 in memo):
                count = count + memo[(60-temp)%60]
            memo[temp] += 1
        return count