# My Rating = 8
# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        strLen=len(s)
        if strLen==0:
            return ""
        dp={}
        maxLength=1
        maxIndex = [0,1]
        for length in range(0,strLen+1):
            for start in range(strLen-length+1):
                if length==0 or length==1:
                    dp[start,length]=True
                else:
					# If the first and last are equal and inner str is a palindrome
                    temp = s[start]==s[start+length-1] and dp[start+1,length-2]
                    dp[start,length] = temp
                    if temp and length>maxLength:
                        maxLength=length
                        maxIndex = [start,length]
        return s[maxIndex[0]:maxIndex[0]+maxIndex[1]]