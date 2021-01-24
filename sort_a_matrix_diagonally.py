# My Rating = 2
# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3614/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        totalDiagonals = m+n-1
        storage = [[] for i in range(totalDiagonals)]
        for i in range(m):
            for j in range(n):
                storage[j-i+m-1].append(mat[i][j])
        for i in range(totalDiagonals):
            storage[i].sort()
        for i in range(m):
            for j in range(n):
                mat[i][j] = storage[j-i+m-1][i if j>i else j]
        return mat