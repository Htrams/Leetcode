# My Rating = 3
# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3517/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        startNode = head
        head = head.next
        while head is not None:
            runningNode = startNode
            while runningNode is not head and runningNode.val<head.val:
                runningNode = runningNode.next
            newVal = head.val
            while runningNode is not head:
                temp = runningNode.val
                runningNode.val = newVal
                newVal = temp
                runningNode = runningNode.next
            runningNode.val = newVal
            head = head.next
        return startNode