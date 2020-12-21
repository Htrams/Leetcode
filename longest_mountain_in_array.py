# My Rating = 3
# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3533/

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        leng = len(A)
        if leng==0:
            return 0
        maxValue=0
        maxLeftCount = 1
        maxRightCount = 0
        downStarted = False
        leftCount=1
        rightCount=0
        preValue = A[0]
        i=1
        while i<leng:
            if A[i]>preValue:
                leftCount += 1
                rightCount = 0
                if downStarted:
                    leftCount = 2
                    downStarted = False
            elif A[i]<preValue:
                rightCount += 1
                downStarted = True
            else:
                leftCount = 1
                rightCount = 0
                downStarted = False
            if leftCount+rightCount>maxValue or (leftCount+rightCount==maxValue and rightCount<leftCount):
                maxValue = leftCount+rightCount
                maxLeftCount = leftCount
                maxRightCount = rightCount
            preValue = A[i]
            i += 1
            # print(leftCount,rightCount)
        # print(maxLeftCount,maxRightCount)
        if maxLeftCount == 1 or maxRightCount == 0:
            maxValue=0
        return maxValue