# My Rating = 6
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3473/
# In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking
# ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned 
# condition.

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        currentPosionEndsAt = 0
        totalPosionTime = 0
        timeLen=len(timeSeries)
        for i in range(timeLen):
            totalPosionTime += duration + (timeSeries[i]-currentPosionEndsAt if timeSeries[i]<currentPosionEndsAt else 0)
            currentPosionEndsAt = timeSeries[i]+duration
        
        return totalPosionTime
            