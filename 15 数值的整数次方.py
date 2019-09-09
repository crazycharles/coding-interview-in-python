# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 15:55:38 2019

@author: an
"""

class Solution(object):
    def Power(self, base, exponent):
        """
        :type base: float
        :type exponent: int
        :rtype: float
        """
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        if exponent > 0:
            return base**exponent
        else:
            return 1/(base**(-exponent))
        