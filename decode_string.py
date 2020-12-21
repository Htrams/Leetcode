# My Rating = 4
# https://leetcode.com/explore/featured/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3536/

from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        for charc in s:
            if charc == ']':
                expres = ''
                while True:
                    temp = stack.pop()
                    if temp == '[':
                        break
                    expres = temp + expres
                itera=0
                unit = 1
                while True:
                    temp = stack.pop()
                    if temp.isalpha() or temp =='[':
                        break
                    itera = itera + int(temp) * unit
                    unit = unit*10
                    if not stack:
                        break
                if stack:
                    stack.append(temp)
                for i in range(itera):
                    stack.append(expres)
            else:
                stack.append(charc)
            # print(stack)
        output=''
        while stack:
            output = output + stack.popleft()
        return output