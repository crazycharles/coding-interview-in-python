# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:31:26 2019

@author: an
"""

class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        map = {}
        if not nums:
            return -1
        if min(nums) < 0 or max(nums) >= len(nums):
            return -1
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                return i
        return -1