# My Rating = 6
# https://leetcode.com/explore/featured/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3538/
# Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. 
# For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.
# Return the number of positive integers that can be generated that are less than or equal to a given integer n.


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        nums = len(digits)
        n = str(n)
        maxDigits = len(n)
        if nums == 1:
            output = maxDigits-1
        else:
            output = int((nums/(nums-1))*(nums**(maxDigits-1) - 1))
        smaller = 0
        itera = maxDigits
        for dig in n:
            itera -= 1
            equal = False
            smaller=0
            for digit in digits:
                if int(digit)<int(dig):
                    smaller = smaller + 1
                elif int(digit)==int(dig):
                    equal = True
            output += smaller*(nums**itera)
            if not equal:
                break
        # if (itera == 0 and maxDigits!=1) or (maxDigits==1 and n[0] in digits):
        #     output += 1
        if itera==0 and n[-1] in digits:
            output += 1
        return output