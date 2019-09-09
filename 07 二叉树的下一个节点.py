# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:56:02 2019

@author: an
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.father = None
class Solution(object):
    def inorderSuccessor(self, q):
        """
        :type q: TreeNode
        :rtype: TreeNode
        """
        cur = q
        right = cur.right
        if right:
            while right:
                pre = right
                right = right.left
            return pre
        while cur.father and cur.father.left != cur:
            cur = cur.father
        return cur.father