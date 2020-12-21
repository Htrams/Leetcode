# My Rating = 4
# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3518/

# Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
# Return the power of the string.

class Solution:
    def maxPower(self, s: str) -> int:
        maxLength = 0
        currentLength = 0
        runningChar = s[0]
        for i in s:
            if runningChar == i:
                currentLength += 1
            else:
                if currentLength > maxLength:
                    maxLength = currentLength
                currentLength = 1
                runningChar = i
        if currentLength > maxLength:
            maxLength = currentLength
        elif maxLength == 0:
            maxLength = 1
        return maxLength
            