# My Rating = 4
# https://leetcode.com/explore/featured/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3521/
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        sumNums = sum(nums)
        active=False
        def binarySearch(up,low,thres,nums,active):
            if up==low+1 or up==low:
                if active:
                    return up
                else:
                    active=True
            currentVal = 0
            currentDiv = (up+low)//2
            for i in nums:
                currentVal += math.ceil(i/currentDiv)
            # print(up,low,currentVal,currentDiv)
            if currentVal>thres:
                # increase Div
                return binarySearch(up,currentDiv,thres,nums,active)
            else:
                # decrease Div
                return binarySearch(currentDiv,low,thres,nums,active)
        return binarySearch(sumNums,1,threshold,nums,active)