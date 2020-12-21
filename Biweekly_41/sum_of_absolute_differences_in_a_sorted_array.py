# My Rating = 3
# https://leetcode.com/contest/biweekly-contest-41/problems/sum-of-absolute-differences-in-a-sorted-array/

# You are given an integer array nums sorted in non-decreasing order.
# Build and return an integer array result with the same length as nums such that result[i] is equal to the summation 
# of absolute differences between nums[i] and all the other elements in the array.

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        runningSum=0
        currentIndex=0
        leng = len(nums)
        sums = sum(nums)
        output = [0]*leng
        while currentIndex<leng:
            output[currentIndex] = currentIndex*nums[currentIndex]-runningSum + sums - runningSum - (leng-currentIndex)*nums[currentIndex]
            runningSum += nums[currentIndex]
            currentIndex += 1
        return output