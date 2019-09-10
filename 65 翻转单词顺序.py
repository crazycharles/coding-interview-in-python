# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:56:45 2019

@author: an
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s = list(s.split())
        new_s = new_s[::-1]
        return " ".join(new_s)