# My Rating = 2 , Follow-up = 5
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3552/

# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
# Follow up:
# What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randint
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.values=[]
        while head is not None:
            self.values.append(head.val)
            head = head.next
        self.length=len(self.values)

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return self.values[randint(0,self.length-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()