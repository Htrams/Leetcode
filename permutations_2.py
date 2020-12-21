# My Rating = 7
# The following code will work but it is highly inefficient.
# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3528/

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

from collections import OrderedDict
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        temp = self.permuteUnique(nums[1:])
        length=len(temp)
        for i in range(length):
            for j in range(len(temp[0])):
                temp.append(temp[0][:j] + [nums[0]] + temp[0][j:])
            temp.append(temp[0]+[nums[0]])
            del temp[0]
        ans=[]
        for i in temp:
            if i not in ans:
                ans.append(i)
        return ans