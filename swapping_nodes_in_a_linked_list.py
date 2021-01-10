# My Rating = 2
# https://leetcode.com/contest/weekly-contest-223/problems/swapping-nodes-in-a-linked-list/
# The following code interchanges the nodes, instead of the values in the node.

# You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values 
# of the kth node from the beginning and the kth node from the 
# end (the list is 1-indexed).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        store = []
        temp = head
        while temp is not None:
            store.append(temp)
            temp = temp.next
        
        leng = len(store)
        k=min(k,leng-k+1)
        
        if leng%2==1 and k==leng//2+1:
            return head
            
        # Edge Cases
        if k==1:
            if leng == 2:
                store[1].next = store[0]
                store[0].next = None
                return store[1]
            else:
                store[-2].next = store[0]
                store[0].next = None
                store[-1].next = store[1]
                return store[-1]
        if leng%2==0 and k==leng//2:
            store[k-2].next = store[k]
            store[k].next = store[k-1]
            store[k-1].next = store[k+1]
            return head
        
        # Swap nodes at k-1 and len(store)-k
        store[k-2].next = store[leng-k]
        store[leng-k].next = store[k]
        store[leng-k-1].next = store[k-1]
        store[k-1].next = store[leng-k+1]
        return head