# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:35:44 2019

@author: an
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSame(root.left, root.right)
    def isSame(self, r1, r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        if r1.val == r2.val:
            return self.isSame(r1.left, r2.right) and self.isSame(r1.right, r2.left)
        else:
            return False