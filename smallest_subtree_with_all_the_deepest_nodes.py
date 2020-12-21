# My Rating = 4
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3563/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def setDepth(node):
            if node.left is not None:
                leftNode = setDepth(node.left)
            else:
                leftNode = 0
            if node.right is not None:
                rightNode = setDepth(node.right)
            else:
                rightNode = 0
            node.depth = max(leftNode,rightNode) + 1
            return node.depth
        def getDeepestSubTree(node):
            if node.left is not None:
                left = node.left.depth
            else:
                left = None
            if node.right is not None:
                right = node.right.depth
            else:
                right = None
            if right == left:
                return node
            elif right is None:
                return getDeepestSubTree(node.left)
            elif left is None:
                return getDeepestSubTree(node.right)
            elif left>right:
                return getDeepestSubTree(node.left)
            else:
                return getDeepestSubTree(node.right)
        setDepth(root)
        return getDeepestSubTree(root)