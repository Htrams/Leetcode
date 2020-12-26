# The following code gives a Time Limit Exceeded Error.
# https://leetcode.com/contest/biweekly-contest-42/problems/maximum-binary-string-after-change/

from collections import deque
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        leng = len(binary)
        if leng==0:
            return ''
        maxVal = 0
        alreadyVisited = set()
        record = deque()
        record.append(binary)
        while record:
            current = record.popleft()
            temp = int(current,2)
            if temp > maxVal:
                maxVal = temp
            alreadyVisited.add(current)
            possible = []
            for i in range(0,leng-1):
                temp = current[i:i+2]
                if temp == '00':
                    possible.append(current[0:i]+'10'+current[i+2:])
                elif temp =='10':
                    possible.append(current[0:i]+'01'+current[i+2:])
            for poss in possible:
                if poss not in alreadyVisited:
                    record.append(poss)
        temp = str(bin(maxVal))[2:]
        return '0' * (leng - len(temp)) + temp