# My Rating = 2
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3553/

# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now 
# the root of the tree, and every node has no left child and only one right child.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inOrderRearrange(node):
            if node.left is not None:
                startingNode, runningNode = inOrderRearrange(node.left)
                runningNode.right = node
            else:
                startingNode = node
            node.left = None
            if node.right is not None:
                node.right,endingNode = inOrderRearrange(node.right)
            else:
                endingNode = node
            return (startingNode,endingNode)
        return inOrderRearrange(root)[0]