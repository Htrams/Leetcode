# My Rating = 4
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3578

# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. 
# If no such positive integer exists, return -1.
# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = str(n)
        leng = len(n)
        i=leng-1
        rec=[]
        flag=False
        while i>=0:
            temp = int(n[i])
            rec.append(temp)
            for j in rec:
                if j>temp:
                    flag=True
                    rec.remove(j)
                    break
            if flag:
                break
            i -= 1
        
        if not flag:
            return -1
        
        temp = ''
        rec.sort()
        for l in rec:
            temp = temp + str(l)
        temp = n[0:i] + str(j) + temp
        if int(temp) > 2147483647:
            return -1
        else:
            return temp