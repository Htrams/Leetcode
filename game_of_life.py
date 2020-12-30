# My Rating = 1
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3586/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        memory = []
        indexDiff=[-1,0,1]
        for i in range(rows):
            for j in range(cols):
                count = 0
                for k in indexDiff:
                    for l in indexDiff:
                        if k==0 and l==0:
                            continue
                        if i+k >= 0 and i+k < rows and j+l >= 0 and j+l < cols:
                            if board[i+k][j+l] == 1:
                                count += 1
                currCell = board[i][j]
                if currCell == 1 and (count<2 or count>3):
                    #dies
                    memory.append((i,j,0))
                elif currCell == 0 and count==3:
                    #lives
                    memory.append((i,j,1))
        for change in memory:
            board[change[0]][change[1]]=change[2]