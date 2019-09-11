# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:20:35 2019

@author: an
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 快慢指针法，先设置两个指针，一个每次走两步，一个每次走一步，直到二者相遇说明有环，否则没有环
# 之后再让一个从头出发，现在两个指针每次都直走一步，二者相遇的地方就是环的入口
class Solution(object):
    def entryNodeOfLoop(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return None
        slow = head.next
        fast = head.next.next
        while slow != fast:
            if slow.next:
                slow = slow.next
            else:
                return None
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return None
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
        
# 占用空间的方法，每次看看这个节点是否重复出现了，如果是，则返回这个节点

class Solution2(object):
    def entryNodeOfLoop(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = []
        cur = head
        while cur:
            if cur not in tmp:
                tmp.append(cur)
            else:
                return cur
            cur = cur.next
        return None    