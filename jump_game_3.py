# My Rating = 5
# https://leetcode.com/explore/featured/card/november-leetcoding-challenge/568/week-5-november-29th-november-30th/3548/
# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at 
# index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
# Notice that you can not jump outside of the array at any time.

from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        leng = len(arr)
        visited = set()
        frontier = deque()
        frontier.append(start)
        while frontier:
            currentNode = frontier.popleft()
            visited.add(currentNode)
            if arr[currentNode] == 0:
                return True
            possValues = (currentNode + arr[currentNode],currentNode - arr[currentNode])
            for possNode in possValues:
                if possNode>=0 and possNode<leng and possNode not in visited:
                    frontier.append(possNode)
        return False