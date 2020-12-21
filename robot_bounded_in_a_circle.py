# My Rating = 5
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3463/

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        direcs = [0,1,2,3]
        # 0 - North, 1 - East, 2 - South, 3 - West
        currX=0
        currY=0
        for i in instructions:
            if i == 'L':
                direction=direcs[direction-1]
            elif i == 'R':
                direction=direcs[(direction+1)%4]
            else:
                if direction==0:
                    currY=currY+1
                elif direction==1:
                    currX=currX+1
                elif direction==2:
                    currY=currY-1
                else:
                    currX=currX-1
        return bool(direction) or (currX==0 and currY==0)