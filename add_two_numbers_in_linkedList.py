# My Rating = 3
# https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carr=0
        pre=None
        while True:
            if l1==None:
                num1=0
            else:
                num1=l1.val
            if l2==None:
                num2=0
            else:
                num2=l2.val
            tempSum=num1+num2+carr
            carr=tempSum//10
            tempSum=tempSum%10
            if carr==0 and tempSum==0 and l1==None and l2==None:
                break
            if pre!=None:
                pre.next = ListNode(tempSum)
                pre=pre.next
            else:
                head=ListNode(tempSum)
                pre=head
            if l1!=None:
                l1=l1.next
            if l2!=None:
                l2=l2.next
        return head
            