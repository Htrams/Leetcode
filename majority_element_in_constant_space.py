# My Rating = 7
# https://leetcode.com/problems/majority-element-ii/submissions/

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Note: The algorithm should run in linear time and in O(1) space.

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        rec={}
        arrLen = len(nums)
        for i in range(arrLen):
            if nums[i] not in rec:
                if len(rec)==2:
                    for j in rec.keys():
                        rec[j] -= 1
                    for j in list(rec.keys()):
                        if rec[j] == 0:
                            del rec[j]
                else:
                    rec[nums[i]] = 1
            else:
                rec[nums[i]] += 1
        output=[]
        for i in rec.keys():
            count=0
            for j in range(arrLen):
                if nums[j]==i:
                    count += 1
            if count > arrLen//3:
                output.append(i)
        return output