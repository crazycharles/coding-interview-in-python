# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:43:15 2019

@author: an
"""

import copy
class Solution(object):
    def getMaxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = copy.deepcopy(grid)
        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, len(grid)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]