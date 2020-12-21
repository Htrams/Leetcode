# My Rating = 4
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3569/

# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

from collections import defaultdict
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        record1=defaultdict(int)
        for i in A:
            for j in B:
                record1[i+j] += 1
        record2=defaultdict(int)
        for i in C:
            for j in D:
                record2[i+j] += 1
        count = 0
        for ele in record1:
            count += record1[ele]*record2[-1*ele]
        return count
        