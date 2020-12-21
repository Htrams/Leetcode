class Solution:
    def stoneGameVI(self, aliceValues, bobValues) -> int:
        memo={}
        def interFunc(values):
            aliceValues,bobValues = values
            leng = len(aliceValues)
            if leng==1:
                return (aliceValues[0],0)
            diff=-100
            for i in range(leng):
                temp=(bobValues[:i]+bobValues[i+1:],aliceValues[:i]+aliceValues[i+1:])
                if temp in memo:
                    val = memo[temp]
                elif (temp[1],temp[0]) in memo:
                    val = memo[temp[1],temp[0]]
                else:
                    val = interFunc(temp)
                if val[1]+aliceValues[i]-val[0]>diff:
                    diff=val[1]+aliceValues[i]-val[0]
                    bestVal=(val[1]+aliceValues[i],val[0])
            return bestVal
        return interFunc((tuple(aliceValues),tuple(bobValues)))

print(Solution().stoneGameVI([9,9,5,5,2,8,2,4,10,2,3,3,4],[9,5,3,4,4,6,6,6,4,3,7,5,10]))