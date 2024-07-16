'''
143. Reorder List
Source: https://leetcode.com/problems/reorder-list/description/
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    # reordering = [0, n-1, 1, n-2, 2, n-3, ...]
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        # O(n)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # [4,5,6,7] => [7,6,5,4]
        # tail.next = tail.prev
        # voor elke node: node.next = node.prev
        # O(n)
        current, prev = slow, None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        # merging the lists
        # O(n)
        first, second = head, prev
        while second.next:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
            


        

            









