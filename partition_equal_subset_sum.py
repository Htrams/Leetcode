# My Rating = 7
# https://leetcode.com/explore/featured/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3545/
# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets 
# such that the sum of elements in both subsets is equal.

from collections import defaultdict
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2!=0:
            return False
        else:
            target = target//2
        dp={0:True}
        for i in range(len(nums)):
            temp=[]
            for j in range(1,target+1):
                if j-nums[i] in dp:
                    temp.append(j)
            for tem in temp:
                dp[tem] = True
            if target in dp:
                return True
        return False