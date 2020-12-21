# My Rating = 2
# Same logic can be used in a 32 bit language
# https://leetcode.com/problems/string-to-integer-atoi/
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

class Solution:
    def myAtoi(self, str: str) -> int:
        INT32_MAX = 2**31-1
        INT32_MIN = -2**31
        numbers={'0','1','2','3','4','5','6','7','8','9'}
        start=0
        neg=1
        num=0
        for i in str:
            if i == ' ':
                if start==1:
                    start=2
                    break
                continue
            elif (i == '-' or i == '+') and start==0:
                start=1
                if i=='-':
                    neg=-1
            elif i in numbers:
                start=1
                print(num)
                if INT32_MAX//10 > num*neg and (-1)*((INT32_MIN*-1)//10) < num*neg:
                    num=num*10+int(i)
                elif INT32_MAX//10 < num * neg:
                    return INT32_MAX
                elif INT32_MIN//10 > num * neg:
                    return INT32_MIN
                elif INT32_MAX//10 == num * neg:
                    if INT32_MAX%10 > int(i):
                        num=num*10+int(i)
                    else:
                        return INT32_MAX
                else:
                    print((-1*INT32_MIN)%10)
                    if (-1*INT32_MIN)%10 > int(i):
                        num=num*10+int(i)
                    else:
                        return INT32_MIN
            else:
                if start==1:
                    start = 2
                    break
                else:
                    # Did not start and is not a number
                    return 0
        return num*neg