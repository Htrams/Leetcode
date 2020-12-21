# My Rating = 7
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3459/
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only 
# constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically 
# contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can 
# rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        numLen = len(nums)
        dp={}
        dp[-1]=0
        for i in range(numLen):
            if i==0:
                dp[0]=nums[0]
                continue
            elif i==1:
                dp[1]=max(nums[0],nums[1])
                continue
            dp[i]=max(
                dp[i-1],
                dp[i-2]+nums[i]
            )
        return dp[numLen-1]