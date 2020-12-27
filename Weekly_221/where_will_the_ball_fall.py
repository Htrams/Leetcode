# My Rating = 6
# https://leetcode.com/contest/weekly-contest-221/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        height = len(grid)
        width = len(grid[0])
        output=[1]*width
        for i in range(width):
            currM,currN = 0,i
            stuck = False
            while currM<height and not stuck:
                if grid[currM][currN] == 1 and currN+1<width and grid[currM][currN+1] == 1:
                    currM += 1
                    currN += 1
                elif grid[currM][currN] == -1 and currN-1>=0 and grid[currM][currN-1] == -1:
                    currM += 1
                    currN -= 1
                else:
                    stuck = True
            if stuck:
                output[i] = -1
            else:
                output[i] = currN
        return output