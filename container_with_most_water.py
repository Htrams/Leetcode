# My Rating = 6
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxWater=0
        while left<right:
            temp=min(height[left],height[right])*(right-left)
            if temp>maxWater:
                maxWater=temp
            if height[left]<height[right]:
                left=left+1
            else:
                right=right-1
        return maxWater