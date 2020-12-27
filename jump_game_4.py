# My Rating = 6
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3582/
# Notice the delete statement (line 32) is essential to optimize the code to not time out.

from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        countItems=len(arr)
        alreadyVisited={}
        itemList={}
        for i in range(countItems):
            if arr[i] not in itemList:
                itemList[arr[i]] = [i]
            else:
                itemList[arr[i]].append(i)

        frontier = deque()
        frontier.append(0)
        alreadyVisited[0]=0
        
        while frontier:
            curr = frontier.popleft()
            if curr == countItems-1:
                return alreadyVisited[curr]
            poss = []
            if curr-1>=0:
                poss.append(curr-1)
            if curr+1<countItems:
                poss.append(curr+1)
            if arr[curr] in itemList:
                poss.extend(itemList[arr[curr]])
                del itemList[arr[curr]]
            for ele in poss:
                if ele not in alreadyVisited:
                    frontier.append(ele)
                    alreadyVisited[ele] = alreadyVisited[curr] + 1
        return -1