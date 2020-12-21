# My Rating = 5
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3467/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        rec = [0]*1001
        for trip in trips:
            rec[trip[1]] += trip[0]
            if rec[trip[1]] > capacity:
                return False
            rec[trip[2]] -= trip[0]
        runningSum = 0
        for i in rec:
            runningSum += i
            if runningSum>capacity:
                return False
        return True