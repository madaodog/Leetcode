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
        length = 0
        current_node = head
        while current_node:
            length += 1
            current_node = current_node.next
        
        second_node = head
        for i in range(length // 2):
            second_node = second_node.next
        
        current_node = head
        for i in range(length // 2):
            temp = current_node.next
            current_node.next = second_node
            second_node.next = temp
        
        return current_node





