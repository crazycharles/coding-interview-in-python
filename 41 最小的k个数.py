# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:21:43 2019

@author: an
"""

class Solution(object):
    def getLeastNumbers_Solution(self, input, k):
        """
        :type input: list[int]
        :type k: int
        :rtype: list[int]
        """
        input.sort()
        return input[:k]