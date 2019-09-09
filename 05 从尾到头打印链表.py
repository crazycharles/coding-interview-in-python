# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:34:28 2019

@author: an
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def printListReversingly(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        cur = head
        if not cur:
            return []
        res = []
        while cur:
            res = [cur.val] + res
            cur = cur.next
        return res