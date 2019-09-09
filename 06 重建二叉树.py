# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:34:46 2019

@author: an
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return []
        root = TreeNode(preorder[0])
        l_inorder = inorder[:inorder.index(root.val)]
        r_inorder = inorder[inorder.index(root.val)+1:]
        l_preorder = preorder[1:len(l_inorder)+1]
        r_preorder = preorder[len(l_inorder)+1:]
        left = self.buildTree(l_preorder, l_inorder)
        right = self.buildTree(r_preorder, r_inorder)
        root.left  = left
        root.right = right
        return root