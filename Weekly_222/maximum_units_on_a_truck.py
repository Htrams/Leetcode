# My Rating = 2
# https://leetcode.com/contest/weekly-contest-222/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1] , reverse=True)
        units=0
        boxes=0
        boxIndex=0
        while boxIndex<len(boxTypes):
            if boxes + boxTypes[boxIndex][0] <= truckSize:
                boxes += boxTypes[boxIndex][0]
                units += boxTypes[boxIndex][1] * boxTypes[boxIndex][0]
            else:
                units += boxTypes[boxIndex][1] * (truckSize-boxes)
                return units
            boxIndex += 1
        return units