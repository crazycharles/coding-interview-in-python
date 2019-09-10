# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:31:00 2019

@author: an
"""

class Solution(object):
    def getNumberSameAsIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == i:
                return i
        return -1