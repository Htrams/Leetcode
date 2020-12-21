# My Rating = 8
# https://leetcode.com/problems/01-matrix/
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.

# BFS Solution. See below for DP solution
from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        cols=len(matrix[0])
        frontier = deque()
        level = {}
        
        # Initialize Start
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    frontier.append((i,j))
                    level[i,j]=0
        
        while frontier:
            currentR,currentC = frontier.popleft()
            #Get Adj
            direcs = [(0,1),(0,-1),(1,0),(-1,0)]
            for direc in direcs:
                adjR,adjC = direc
                adjR += currentR
                adjC += currentC
                if adjR>=0 and adjR<rows and adjC>=0 and adjC<cols:
                    if (adjR,adjC) not in level:
                        matrix[adjR][adjC] = level[adjR,adjC] = level[currentR,currentC] + 1
                        frontier.append((adjR,adjC))
        return matrix



# DP solution.
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        cols=len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    continue
                temp = float('inf')
                if j>=1:
                    temp = min(temp,matrix[i][j-1])
                if i>=1:
                    temp = min(temp,matrix[i-1][j])
                matrix[i][j]=temp+1
        
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if matrix[i][j]==0:
                    continue
                temp = matrix[i][j]
                if j+1<cols:
                    temp = min(temp,matrix[i][j+1]+1)
                if i+1<rows:
                    temp = min(temp,matrix[i+1][j]+1)
                matrix[i][j]=temp
        return matrix