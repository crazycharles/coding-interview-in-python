# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:40:15 2019

@author: an
"""

class Solution(object):
    def NumberOf1(self,n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        for i in range(32):
            counter += n & 1
            n = n // 2
        return counter