'''
19. Remove Nth Node From End of List
Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        
        # Step 1: Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Find the node just before the one we need to remove
        current = dummy
        for _ in range(length - n):
            current = current.next
        
        # Step 3: Remove the nth node from the end
        current.next = current.next.next
        
        # Return the modified list
        return dummy.next


        