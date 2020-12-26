# My Rating = 4
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3581/

class Solution:
    def numDecodings(self, s: str) -> int:
        dp={}
        dp[-1] = 1
        if s[0] == '0':
            return 0
        else:
            dp[0] = 1
        for i in range(1,len(s)):
            dp[i] = dp[i-1] * (0 < int(s[i]) < 27) + dp[i-2] * (0 < int(s[i-1]+s[i]) < 27) * (s[i-1] != '0')
            del dp[i-2]
        return dp[len(s)-1]