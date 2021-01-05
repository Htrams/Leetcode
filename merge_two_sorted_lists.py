# My Rating = 1
# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3592/

# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        outputHead=ListNode()
        temp = outputHead
        while l1 is not None and l2 is not None:
            if l1.val>l2.val:
                temp.next = l2
                temp = temp.next
                l2 = l2.next
            else:
                temp.next = l1
                temp = temp.next
                l1 = l1.next
        while l1 is not None:
            temp.next = l1
            temp = temp.next
            l1 = l1.next
        while l2 is not None:
            temp.next = l2
            temp = temp.next
            l2 = l2.next
        return outputHead.next