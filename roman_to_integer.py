# My Rating = 1
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        value={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M':1000
        }
        finalValue=0
        strLen=len(s)
        for j in range(strLen-1):
            i=s[j]
            if value[i] >= value[s[j+1]] :
                finalValue=finalValue+value[i]
            else:
                finalValue=finalValue-value[i]
        finalValue=finalValue+value[s[-1]]
        return finalValue