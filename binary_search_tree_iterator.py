# My Rating = 2
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3560/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        def inOrderTraversal(output,node):
            if node.left is not None:
                output.extend(inOrderTraversal([],node.left))
            output.append(node.val)
            if node.right is not None:
                output.extend(inOrderTraversal([],node.right))
            return output
        self.output=inOrderTraversal([],root)
        self.currentNode = -1

    def next(self) -> int:
        self.currentNode += 1
        return self.output[self.currentNode]

    def hasNext(self) -> bool:
        return self.currentNode+1<len(self.output)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()