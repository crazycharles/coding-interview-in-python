# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:54:25 2019

@author: an
"""

class Solution(object):
    def findNumbersWithSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            if target - i in nums:
                return [i, target - i]