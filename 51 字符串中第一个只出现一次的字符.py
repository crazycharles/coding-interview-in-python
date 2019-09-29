# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 19:38:46 2019

@author: an
"""

class Solution:
    def firstNotRepeatingChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_map = {}
        for i in s:
            if i not in char_map:
                char_map[i] = 1
            else:
                char_map[i] += 1
        for i in s:
            if char_map[i] == 1:
                return i
        return "#"