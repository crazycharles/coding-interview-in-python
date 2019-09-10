# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:34:52 2019

@author: an
"""

class Solution(object):
    def leftRotateString(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:]+s[:n]