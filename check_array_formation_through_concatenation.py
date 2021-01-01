# My Rating = 3
# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3589/

# You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. 
# Your goal is to form arr by concatenating the arrays in pieces in any order. 
# However, you are not allowed to reorder the integers in each array pieces[i].
# Return true if it is possible to form the array arr from pieces. Otherwise, return false.

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        startValues={}
        i=0
        while i<len(pieces):
            startValues[pieces[i][0]] = i
            i+=1
        i=0
        while i<len(arr):
            if arr[i] not in startValues:
                return False
            temp = pieces[startValues[arr[i]]]
            for j in temp:
                if j != arr[i]:
                    return False
                i+=1
        return True