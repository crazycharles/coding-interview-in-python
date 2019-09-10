# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:23:38 2019

@author: an
"""

class Solution(object):
    def moreThanHalfNum_Solution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        m = len(nums)//2
        return nums[m]