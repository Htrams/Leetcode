# My Rating = 1
# Not the best solution
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3554/

# Given two positive integers n and k.
# A factor of an integer n is defined as an integer i where n % i == 0.
# Consider a list of all factors of n sorted in ascending order, 
# return the kth factor in this list or return -1 if n has less than k factors.

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for i in range(1,n+1):
            if n%i==0:
                count += 1
            if count==k:
                return i
        return -1