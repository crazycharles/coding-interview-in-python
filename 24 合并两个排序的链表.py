# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:59:20 2019

@author: an
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1
        cur2 = l2
        dummy = ListNode(-1)
        new_cur = dummy
        while cur1 and cur2:
            if cur1.val < cur2.val:
                new_cur.next = cur1
                cur1 = cur1.next
                new_cur = new_cur.next
            else:
                new_cur.next = cur2
                cur2 = cur2.next
                new_cur = new_cur.next
        while cur1:
            new_cur.next = cur1
            new_cur = new_cur.next
            cur1 = cur1.next
        while cur2:
            new_cur.next = cur2
            new_cur = new_cur.next
            cur2 = cur2.next 
        return dummy.next