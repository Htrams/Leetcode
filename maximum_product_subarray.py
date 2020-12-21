# My Rating = 7
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3456/
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp={}
        arrLen=len(nums)
        globalMax=nums[0]
        dp[0]=[nums[0],nums[0]]
        for i in range(1,arrLen):
            dp[i]=[max(
                    dp[i-1][0]*nums[i],
                    dp[i-1][1]*nums[i],
                    nums[i]
                   ),
                   min(
                    dp[i-1][0]*nums[i],
                    dp[i-1][1]*nums[i],
                    nums[i]
                   )
                  ]
            if dp[i][0]>globalMax:
                globalMax=dp[i][0]
            del dp[i-1]
        return globalMax
        