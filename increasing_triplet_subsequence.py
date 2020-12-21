# My Rating = 3
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3570/

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
# If no such indices exists, return false.

from math import inf
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        rec=[inf,inf]
        for num in nums:
            if rec[0] > num:
                rec[0]=num
            if rec[0]<num and rec[1]>num:
                rec[1]=num
            if num>rec[1]:
                return True
        return False