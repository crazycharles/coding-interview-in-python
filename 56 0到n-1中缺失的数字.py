# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:51:22 2019

@author: an
"""

class Solution(object):
    def getMissingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)