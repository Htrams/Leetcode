# My Rating = 3
# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3535

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array 
# of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        output=[]
        start=intervals[0][0]
        end=intervals[0][1]
        leng=len(intervals)
        i=1
        while i<leng:
            if intervals[i][0]<=end:
                if intervals[i][1]<=end:
                    pass
                else:
                    end=intervals[i][1]
            elif intervals[i][1]>end:
                output.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
            i += 1
        output.append([start,end])
        return output
                    