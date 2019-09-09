# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:31:02 2019

@author: an
"""

class Solution(object):
    def replaceSpaces(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.replace(" ", "%20")
        return s

h = Solution()
s = "adfa ds"
r = h.replaceSpaces(s)    
print(r)