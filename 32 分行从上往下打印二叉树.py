# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:54:50 2019

@author: an
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printFromTopToBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        root_stack = [root]
        leaf_stack = [[root.val]]
        while root_stack:
            temp_root = []
            temp_leaf = []
            for i in root_stack:
                if i.left:
                    temp_root.append(i.left)
                    temp_leaf.append(i.left.val)
                if i.right:
                    temp_root.append(i.right)
                    temp_leaf.append(i.right.val)
            if temp_leaf:
                leaf_stack.append(temp_leaf)
            root_stack = temp_root
        return leaf_stack
                    
                    