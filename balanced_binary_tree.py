# My Rating = 1
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3577/

# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def isBal(node):
            if node is None:
                return 0
            left = isBal(node.left)
            right = isBal(node.right)
            if left is None or right is None:
                return None
            if abs(left-right) < 2:
                return max(left,right) + 1
            else:
                return None
        if isBal(root) is not None:
            return True
        else:
            return False