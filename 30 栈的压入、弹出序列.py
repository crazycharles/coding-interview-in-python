# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:09:58 2019

@author: an
"""

class Solution(object):
    def isPopOrder(self, pushV, popV):
        """
        :type pushV: list[int]
        :type popV: list[int]
        :rtype: bool
        """
        stack = []
        if len(pushV) != len(popV):
            return False
        for i in pushV:
            stack.append(i)
            while len(stack) != 0 and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(popV) > 0:
            return False
        else:
            return True
        