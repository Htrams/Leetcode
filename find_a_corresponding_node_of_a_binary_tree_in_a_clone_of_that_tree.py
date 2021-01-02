# My Rating = 2
# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3590/

# Given two binary trees original and cloned and given a reference to a node target in the original tree.
# The cloned tree is a copy of the original tree.
# Return a reference to the same node in the cloned tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned
        if original.left is not None:
            temp = self.getTargetCopy(original.left,cloned.left,target)
            if temp is not None:
                return temp
        if original.right is not None:
            temp = self.getTargetCopy(original.right,cloned.right,target)
            if temp is not None:
                return temp
        return None