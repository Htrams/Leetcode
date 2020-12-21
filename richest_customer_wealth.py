# My Rating = 1
# https://leetcode.com/contest/weekly-contest-217/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])