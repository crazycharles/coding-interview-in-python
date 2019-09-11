# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:35:22 2019

@author: an
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirror(self, root):
        """
        :type root: TreeNode
        :rtype: void
        """
        if not root:
            return root
        left = root.left
        right = root.right
        new_right = self.mirror(left)
        new_left = self.mirror(right)
        root.left = new_left
        root.right = new_right
        return root