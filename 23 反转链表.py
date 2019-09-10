# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:52:16 2019

@author: an
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        pre = None
        cur = head
        while cur.next:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        cur.next = pre
        return cur