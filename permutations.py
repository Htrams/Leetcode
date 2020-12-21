# My Rating = 2
# https://leetcode.com/problems/permutations/
# Given a collection of distinct integers, return all possible permutations.
class Solution:
    def permute(self, nums):
        if len(nums)==1:
            return [nums]
        temp = self.permute(nums[1:])
        length=len(temp)
        for i in range(length):
            for j in range(len(temp[0])):
                temp.append(temp[0][:j] + [nums[0]] + temp[0][j:])
            temp.append(temp[0]+[nums[0]])
            del temp[0]
        return temp