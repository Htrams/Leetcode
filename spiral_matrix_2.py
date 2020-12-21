# My Rating = 2
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3557/

# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0 for i in range(n)] for j in range(n)]
        direction = 0
        currentRow = 0
        currentCol = 0
        output[0][0] = 1
        currentVal = 2
        i=0
        j=0
        while currentVal<=n**2:
            if direction == 0:
                #go right
                j += 1
            elif direction == 1:
                #go down
                i += 1
            elif direction == 2:
                #go left
                j -= 1
            elif direction == 3:
                #go up
                i -= 1
            output[i][j] = currentVal
            # print(i,j)
            currentVal += 1
            if direction==0 and (j==n-1 or output[i][j+1] != 0):
                direction=1
            elif direction==1 and (i==n-1 or output[i+1][j] != 0):
                direction=2
            elif direction==2 and (j==0 or output[i][j-1] != 0):
                direction=3
            elif direction==3 and (i==0 or output[i-1][j] != 0):
                direction=0
        return output