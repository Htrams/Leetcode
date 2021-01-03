# My Rating = 3
# https://leetcode.com/contest/weekly-contest-222/problems/count-good-meals/

# A good meal is a meal that contains exactly two different food items with 
# a sum of deliciousness equal to a power of two.
# You can pick any two different foods to make a good meal.
# Given an array of integers deliciousness where deliciousness[i] is the deliciousness 
# of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from 
# this list modulo 109 + 7.

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powerOf2 = 1
        count = 0
        while powerOf2 < 2097153:
            rec={}
            for i in deliciousness:
                if powerOf2-i in rec:
                    count += rec[powerOf2-i]
                if i in rec:
                    rec[i] += 1
                else:
                    rec[i] = 1
            powerOf2 *= 2
        return count%(10**9+7)