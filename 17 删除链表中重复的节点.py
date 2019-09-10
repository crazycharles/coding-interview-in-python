# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:36:47 2019

@author: an
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplication(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #定义一个空指针，防止第一个节点和第二个节点就重复
        dummy = ListNode(-1)
        dummy.next = head
        #pre指针是已经确定的不重复节点
        #cur指针是当前要判断的节点
        pre = dummy
        cur = dummy.next
        while cur:
            # 如果重复，就一直后移直到两个指针不重复
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return dummy.next