# My Rating = 2
# Note - Since python supports large numbers higher than 32 bit, this question becomes trivial. Same code can be easily converted for a 32 bit language.
# https://leetcode.com/problems/reverse-integer/
# Given a 32-bit signed integer, reverse digits of an integer.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows

class Solution:
    def reverse(self, x: int) -> int:
        x=list(str(x))
        if x[0]=='-':
            start=1
        else:
            start=0
        end=len(x)-1
        while start<end:
            temp=x[start]
            x[start]=x[end]
            x[end]=temp
            start=start+1
            end=end-1
        final=''
        for i in x:
            final=final+i
        final = int(final)
        if final>2147483647 or final < -2147483648:
            return 0
        else:
            return final