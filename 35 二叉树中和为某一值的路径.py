# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:38:21 2019

@author: an
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findPath(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return []
        if not root.left and not root.right and root.val == sum:
            return [[root.val]]
        left = self.findPath(root.left, sum - root.val)
        right = self.findPath(root.right, sum - root.val)
        for i in left + right:
            res.append([root.val] + i)
        return res