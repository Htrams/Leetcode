# My Rating = 1
# https://leetcode.com/problems/distribute-candies/
# You have n candies, the ith candy is of type candies[i].
# You want to distribute the candies equally between a sister and a brother so that each of them gets 
# n / 2 candies (n is even). The sister loves to collect different types of candies, so you want to 
# give her the maximum number of different types of candies.
# Return the maximum number of different types of candies you can give to the sister.

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        rec=set()
        count=0
        for i in candies:
            if i not in rec:
                rec.add(i)
                count += 1
        return min(len(candies)//2 , count)