# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:13:06 2019

@author: an
"""

class Solution(object):
    def isContinuous(self, numbers):
        """
        :type numbers: List[int]
        :rtype: bool
        """
        if len(numbers) == 0:
            return False
        zero_lst = []
        orig_lst = []
        for i in numbers:
            if i == 0:
                zero_lst.append(i)
            else:
                orig_lst.append(i)
        orig_lst.sort()
        if len(set(orig_lst)) != len(orig_lst):
            return False
        if orig_lst[-1] - orig_lst[0] <= 4:
            return True
        else:
            return False