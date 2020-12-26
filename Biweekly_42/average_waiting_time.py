# My Rating = 2
# https://leetcode.com/contest/biweekly-contest-42/problems/average-waiting-time/

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        totalWaitTime = 0
        currentTime = customers[0][0]
        for customer in customers:
            totalWaitTime += customer[1] + max((currentTime - customer[0]),0)
            currentTime = max(currentTime + customer[1],customer[0]+customer[1])
        return totalWaitTime/len(customers)