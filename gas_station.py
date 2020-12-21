# My Rating = 7
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3470/
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
# You begin the journey with an empty tank at one of the gas stations.
# Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arrLen = len(gas)
        runningValue = 0
        totalValue = 0
        out = -1
        for i in range(arrLen):
            totalValue = totalValue + gas[i] - cost[i]
            runningValue = runningValue + gas[i] - cost[i]
            if runningValue>=0 and out == -1:
                out = i
            elif runningValue<0:
                out = -1
                runningValue=0
        if totalValue<0:
            return -1
        else:
            return out