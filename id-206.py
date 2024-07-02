'''
206. Reverse Linked List
Source: https://leetcode.com/problems/reverse-linked-list/
'''
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while(current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head


        
        