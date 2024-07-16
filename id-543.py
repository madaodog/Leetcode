'''
543. Diameter of Binary Tree
Source: https://leetcode.com/problems/diameter-of-binary-tree/description/
'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # Initialize the diameter

        def length_of_tree(node):
            if not node:
                return 0
            
            # Get the lengths of the left and right subtrees
            left_length = length_of_tree(node.left)
            right_length = length_of_tree(node.right)
            
            # Update the diameter
            self.diameter = max(self.diameter, left_length + right_length)
            
            # Return the length of the longest path
            return 1 + max(left_length, right_length)

        length_of_tree(root)  # Call the helper function
        return self.diameter

    

s = Solution()
t = TreeNode()
print(s.diameterOfBinaryTree(t))
    

