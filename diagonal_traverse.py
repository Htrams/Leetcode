# My Rating = 2
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3580/

# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        if M==0:
            return []
        N = len(matrix[0])
        output = [0]*(M*N)
        
        inBounds = lambda m,n : m<M and m>=0 and n<N and n>=0
        count = 0
        
        currM=0
        currN=0
        goingUp = True
        
        def move(goingUp,currM,currN):
            if goingUp:
                currM -= 1
                currN += 1
            else:
                currM += 1
                currN -= 1
            return currM,currN
        
        while count!=M*N:
            if not inBounds(currM,currN):
                currM += 1
                goingUp = not goingUp
                while not inBounds(currM,currN):
                    currM,currN = move(goingUp,currM,currN)
            output[count] = matrix[currM][currN]
            count += 1
            currM,currN = move(goingUp,currM,currN)
        
        return output