# My Rating = 8
# https://leetcode.com/problems/permutation-sequence/
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# Given n and k, return the kth permutation sequence.


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digitsRem = [str(i) for i in range(1,n+1)]
        fact = [1,1,2,6,24,120,720,5040,40320,362880] #Stores factorial. Can also be calculated
        output = ""
        rem = k-1
        for i in range(n-1,-1,-1):
            quot = rem//fact[i]
            output = output + digitsRem[quot]
            del digitsRem[quot]
            rem = rem % fact[i]
        return output