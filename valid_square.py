# My Rating = 4
# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3527/

# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.
# The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        value1 = None
        value2 = None
        pairCoord = [(p1,p2),(p1,p3),(p1,p4),(p2,p3),(p2,p4),(p3,p4)]
        distance = []
        for pair in pairCoord:
            distance.append( (pair[0][0]-pair[1][0])**2 + (pair[0][1]-pair[1][1])**2 )
        for val in distance:
            if value1 is None:
                value1 = val
            elif value1 == val:
                pass
            elif value2 is None:
                value2 = val
            elif value2 == val:
                pass
            else:
                return False
        return (value1 is not None) and (value2 is not None) and ((value1<value2 and value1*2==value2) or (value1>value2 and value2*2==value1))