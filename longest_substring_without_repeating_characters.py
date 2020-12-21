# My Rating = 8
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strLen=len(s)
        globalMax=0
        i=0
        
        while i < strLen:
            record={}
            runningMax=0
            for j in range(i,strLen):
                if s[j] in record:
                    if runningMax>globalMax:
                        globalMax=runningMax
                    i=record[s[j]]
                    break
                else:
                    record[s[j]]=j
                    runningMax=runningMax+1
            i=i+1
            if runningMax>globalMax:
                globalMax=runningMax
                break
        return globalMax