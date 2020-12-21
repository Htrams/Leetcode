# My Rating = 3
# https://leetcode.com/contest/weekly-contest-206/problems/special-positions-in-a-binary-matrix/
# Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.
# A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows=len(mat)
        cols=len(mat[0])
        count=0
        for i in range(rows):
            flag=0
            ind=-1
            for j in range(cols):
                if mat[i][j]==1:
                    if flag==0:
                        flag=1
                        ind=j
                    else:
                        flag=2
                        break
            if flag==1:
                flag=0
                for k in range(rows):
                    if mat[k][ind]==1:
                        if flag==0:
                            flag=1
                        else:
                            flag=2
                            break
                if flag==1:
                    count=count+1
        return count