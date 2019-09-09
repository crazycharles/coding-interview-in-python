# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 15:56:27 2019

@author: an
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void 
        """
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
        else:
            node = None