# The following code does not work

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        leng=len(nums)
        i=0
        j=0
        rec={}
        runningSum=0
        maxValue=0
        while i<leng:
            print(i,j,runningSum,rec)
            runningSum += nums[i]
            if nums[i] in rec and rec[nums[i]][0]>=j:
                j=rec[nums[i]][0]+1
                runningSum -= rec[nums[i]][1]
            rec[nums[i]]=(i,runningSum)
            i+=1
            if runningSum>maxValue:
                maxValue=runningSum
        return maxValue