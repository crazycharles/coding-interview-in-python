# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:59:39 2019

@author: an
"""

class Solution(object):
    def maxDiff(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0 for i in range(len(nums))]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], nums[i] - nums[i-1] + dp[i-1])
        return max(dp)