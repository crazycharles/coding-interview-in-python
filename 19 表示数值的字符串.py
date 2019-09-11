# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:56:19 2019

@author: an
"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except:
            return False
        