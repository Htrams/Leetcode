# My Rating = 1
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3579/

# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes. Only nodes itself may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = None
        if head is not None and head.next is not None:
            temp = head
            head = head.next
            temp.next = head.next
            head.next = temp
            prev=head.next
        while prev is not None and prev.next is not None and prev.next.next is not None:
            curHead = prev.next
            prev.next = curHead.next
            curHead.next = prev.next.next
            prev.next.next = curHead
            prev = prev.next.next
        return head