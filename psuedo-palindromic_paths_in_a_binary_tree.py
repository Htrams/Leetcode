# My Rating = 1
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3585/

# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic 
# if at least one permutation of the node values in the path is a palindrome.
# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def graphTraversal(node,record):
            record[node.val-1] += 1
            temp = 0
            if node.left is not None:
                temp += graphTraversal(node.left,record)
            if node.right is not None:
                temp += graphTraversal(node.right,record)
            if node.left is None and node.right is None:
                flag=False
                odds = 0
                for ele in record:
                    if ele%2==1:
                        odds+=1
                        if odds>1:
                            flag = True
                            break
                if not flag:
                    temp = 1
            record[node.val-1] -= 1
            return temp

        record=[0]*9
        return graphTraversal(root,record)