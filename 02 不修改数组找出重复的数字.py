# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:01:56 2019

@author: an
"""

class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        n = len(nums) - 1
        l = 1
        r = n
        while l < r:
            m = (l + r + 1)//2
            l_num = 0
            r_num = 0
            for i in nums:
                if i < m:
                    l_num += 1
                else:
                    r_num += 1
            if l_num >= m:
                r = m - 1
            else:
                l = m
        return l