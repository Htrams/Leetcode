# My Rating = 4
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3555/

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers 
# can be planted in the flowerbed without violating the no-adjacent-flowers rule.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possForFlower = 0
        firstOne = False
        adjacentZeros = 0
        for i in flowerbed:
            if i==0:
                adjacentZeros += 1
            else:
                if adjacentZeros%2==0:
                    possForFlower += adjacentZeros//2 - 1*(firstOne==True)
                else:
                    possForFlower += adjacentZeros//2
                firstOne = True
                adjacentZeros=0
        if adjacentZeros:
            if adjacentZeros%2==0:
                possForFlower += adjacentZeros//2
            else:
                possForFlower += adjacentZeros//2 + 1*(firstOne==False)
        if possForFlower>=n:
            return True
        return False