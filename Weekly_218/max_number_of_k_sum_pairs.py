# My Rating = 2
# https://leetcode.com/contest/weekly-contest-218/problems/max-number-of-k-sum-pairs/

# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from 
# the array.
# Return the maximum number of operations you can perform on the array.

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        rec = {}
        count = 0
        for num in nums:
            if k-num in rec:
                rec[k-num] -= 1
                count += 1
                if rec[k-num] == 0:
                    del rec[k-num]
            else:
                if num in rec:
                    rec[num]+=1
                else:
                    rec[num] = 1
        return count