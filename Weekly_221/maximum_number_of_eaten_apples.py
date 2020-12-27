# My Rating = 7
# code can be refactored to be more readable
# https://leetcode.com/contest/weekly-contest-221/problems/maximum-number-of-eaten-apples/

import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # record = {}
        record = []
        maxDays = 0
        for day in range(len(apples)):
            heapq.heappush(record,(day+days[day]-1,apples[day]))
            temp = heapq.heappop(record)
            while (temp[0]<day or temp[1]<=0) and record:
                temp = heapq.heappop(record)
            if temp[0]>=day:
                if temp[1]>1:
                    heapq.heappush(record,(temp[0],temp[1]-1))
                maxDays += 1
        
        while record:
            day += 1
            temp = heapq.heappop(record)
            while (temp[0]<day or temp[1]<=0) and record:
                temp = heapq.heappop(record)
            if temp[0]>=day:
                if temp[1]>1:
                    heapq.heappush(record,(temp[0],temp[1]-1))
                maxDays += 1
        return maxDays