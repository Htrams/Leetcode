# My Rating = 8
# https://leetcode.com/contest/biweekly-contest-34/problems/number-of-ways-to-split-a-string/
# Given a binary string s (a string consisting only of '0's and '1's), we can split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).
# Return the number of ways s can be split such that the number of characters '1' is the same in s1, s2, and s3.
# Since the answer may be too large, return it modulo 10^9 + 7.

from collections import defaultdict
class Solution:
    def numWays(self, s: str) -> int:
        strlength=len(s)
        noOfOnes=0
        record=defaultdict(int)
        for i in range(strlength):
            if s[i]=='1':
                noOfOnes=noOfOnes+1
                record[noOfOnes]=i
        if noOfOnes%3!=0:
            temp = 0
        elif noOfOnes==0:
            temp = (strlength-1)*(strlength-2)//2
        else:
            temp = (record[noOfOnes//3+1]-record[noOfOnes//3])*(record[2*noOfOnes//3+1]-record[2*noOfOnes//3])
        return temp%1000000007