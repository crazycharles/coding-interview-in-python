# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:28:14 2019

@author: an
"""

class Solution(object):
    def Fibonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [0, 1]
        if n <= 1:
            return a[n]
        for i in range(1, n):
            a.append(a[-1]+a[-2])
        return a[-1]