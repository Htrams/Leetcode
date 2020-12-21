# My Rating = 5
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# Follow up: The overall run time complexity should be O(log (m+n)).

import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list1Len=len(nums1)
        list2Len=len(nums2)
        list1Pos=0
        list2Pos=0
        combinedPos=0
        combinedLength=list1Len+list2Len
        preValue=-1
        while True:
            if combinedPos==(combinedLength)//2:
                if list1Pos >= list1Len:
                    value1=math.inf
                else:
                    value1=nums1[list1Pos]
                if list2Pos >= list2Len:
                    value2=math.inf
                else:
                    value2=nums2[list2Pos]
                break
            if list1Pos >= list1Len:
                value1=math.inf
            else:
                value1=nums1[list1Pos]
            if list2Pos >= list2Len:
                value2=math.inf
            else:
                value2=nums2[list2Pos]

            if value1<value2:
                list1Pos=list1Pos+1
                preValue=value1
                combinedPos=combinedPos+1
            else:
                list2Pos=list2Pos+1
                preValue=value2
                combinedPos=combinedPos+1
            
        if combinedLength%2==0:
            return (preValue+min(value1,value2))/2
        else:
            return min(value1,value2)
