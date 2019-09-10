# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:35:54 2019

@author: an
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def findKthToTail(self, pListHead, k):
        """
        :type pListHead: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not pListHead:
            return None
        pre = pListHead
        cur = pListHead
        for i in range(k-1):
            if cur.next:
                cur = cur.next
            else:
                return None
        while cur.next:
            pre = pre.next
            cur = cur.next
        return pre
