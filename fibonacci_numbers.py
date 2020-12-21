# My Rating = 1
# https://leetcode.com/problems/fibonacci-number/
# Given N, calculate F(N)

class Solution:
    def fib(self, N: int) -> int:
        dp={0:0,1:1}
        for i in range(2,N+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[N]