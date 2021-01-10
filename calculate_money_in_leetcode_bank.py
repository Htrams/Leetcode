# My Rating = 1
# https://leetcode.com/contest/biweekly-contest-43/problems/calculate-money-in-leetcode-bank/

# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, 
# he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

class Solution:
    def totalMoney(self, n: int) -> int:
        output = 0
        dailyMoney = 6
        for i in range(1,n+1):
            dailyMoney += 1
            if i%7 == 1:
                dailyMoney = dailyMoney - 7 + 1
            output += dailyMoney
        return output