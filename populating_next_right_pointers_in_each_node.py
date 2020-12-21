# My Rating = 6
# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3529/

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        currentNode = root
        while currentNode.left is not None:
            runningNode = currentNode.left
            temp=currentNode
            while runningNode is not None:
                runningNode.next = temp.right
                runningNode = runningNode.next
                runningNode.next = temp.next.left if temp.next is not None else None
                runningNode = runningNode.next
                temp=temp.next
            currentNode=currentNode.left
        return root