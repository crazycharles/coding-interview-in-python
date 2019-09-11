# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:29:09 2019

@author: an
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasSubtree(self, pRoot1, pRoot2):
        """
        :type pRoot1: TreeNode
        :type pRoot2: TreeNode
        :rtype: bool
        """
        if not pRoot2 or not pRoot1:
            return False
        if self.isSame(pRoot1, pRoot2):
            return True
        return self.hasSubtree(pRoot1.left, pRoot2) or self.hasSubtree(pRoot1.right, pRoot2)
            
        
    def isSame(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val == root2.val:
            return self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right)
        else:
            return False