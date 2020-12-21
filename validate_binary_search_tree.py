# My Rating = 3
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3568/

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inOrderTraversal(node,cB):
            if node.left is not None:
                cB = inOrderTraversal(node.left,cB)
            if cB>=node.val or cB==math.inf:
                return math.inf
            cB=node.val
            if node.right is not None:
                cB = inOrderTraversal(node.right,cB) 
            return cB
        if inOrderTraversal(root,math.inf*-1) != math.inf:
            return True
        return False