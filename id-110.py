'''
110. Balanced Binary Tree
Source: https://leetcode.com/problems/balanced-binary-tree/description/
'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def height_of_tree(root):
            if root is None:
                return 0
            
            left_height = height_of_tree(root.left)
            right_height = height_of_tree(root.right)

            if abs(left_height - right_height) > 1:
                return -1
            
            return 1+max(left_height, right_height)

        if not (-1 <= height_of_tree(root.left) - height_of_tree(root.right) <= 1):
            return False
        
        return height_of_tree(root) != -1