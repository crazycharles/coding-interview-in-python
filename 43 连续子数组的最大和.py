# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:49:18 2019

@author: an
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [i for i in nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        return max(dp)