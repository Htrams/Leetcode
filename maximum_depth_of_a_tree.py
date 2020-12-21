# My Rating = 1
# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        temp=0
        if root.left is not None and root.right is not None:
            temp=max(
                self.maxDepth(root.left),
                self.maxDepth(root.right)
            ) + 1
        elif root.left is None and root.right is not None:
            temp=self.maxDepth(root.right)+1
        elif root.right is None and root.left is not None:
            temp=self.maxDepth(root.left)+1
        else:
            temp=1
        return temp