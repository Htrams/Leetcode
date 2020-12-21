# My Rating = 6
# https://leetcode.com/contest/weekly-contest-215/problems/minimum-operations-to-reduce-x-to-zero/

import math
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        frontDic = {}
        backDic = {}
        runningSum = 0
        index=1
        for num in nums:
            runningSum += num
            frontDic[runningSum]=index
            index+=1
        runningSum = 0
        index=1
        for num in reversed(nums):
            runningSum += num
            backDic[runningSum] = index
            index+=1
        
        minValue = math.inf
        for num in frontDic:
            if num==x:
                minValue = min(minValue,frontDic[num])
            elif (x-num) in backDic and len(nums)-backDic[x-num]+1>frontDic[num]:
                minValue = min(minValue,backDic[x-num]+frontDic[num])
        if x in backDic:
            minValue = min(minValue,backDic[x])
        
        if minValue == math.inf:
            return -1
        return minValue