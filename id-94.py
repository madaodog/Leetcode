'''
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/description/
'''
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list = []
        def helper(root):
            if root != None:
                helper(root.left)
                list.append(root.val)
                helper(root.right)
            else:
                return
        helper(root)
        return list
