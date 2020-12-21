# My Rating = 3
# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3522/

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first 
# and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1=0
        num2=0
        while l1 is not None:
            num1 = num1*10 + l1.val
            l1 = l1.next
        while l2 is not None:
            num2 = num2*10 + l2.val
            l2 = l2.next
        num3=str(num1+num2)
        l3 = ListNode()
        l3.val=int(num3[0])
        head=l3
        for dig in num3[1:]:
            l3.next = ListNode()
            l3=l3.next
            l3.val = int(dig)
        return head
            
        