# My Rating = 2
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3562/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newLength=0
        shiftBy=0
        prevNum = -100000
        reps = 0
        index = 0
        while index<len(nums):
            num = nums[index]
            if num != prevNum:
                reps=1
                prevNum=num
            else:
                reps += 1
                if reps>2:
                    shiftBy += 1
                    newLength -= 1
            newLength += 1
            nums[index-shiftBy] = num
            index += 1
        return newLength