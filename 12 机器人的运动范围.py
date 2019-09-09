# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:40:37 2019

@author: an
"""

class Solution(object):
    def movingCount(self, threshold, rows, cols):
        """
        :type threshold: int
        :type rows: int
        :type cols: int
        :rtype: int
        """
        self.rows = rows
        self.cols = cols
        self.threshold = threshold
        self.memory = {}
        return self.dfs(0, 0)
    def dfs(self, x, y):
        if not self.is_valid(x, y):
            return 0
        res = 0
        if (x, y) in self.memory:
            return 0
        self.memory[(x, y)] = 1
        return self.dfs(x - 1, y) + self.dfs(x + 1, y) + self.dfs(x, y - 1) + self.dfs(x, y + 1) + 1
    def is_valid(self, x, y):
        if x < self.rows and x >= 0 and y < self.cols and y >= 0 and self.digitSum(x) + self.digitSum(y) <= self.threshold:
            return True
        else:
            return False
    def digitSum(self, i):
        res = 0
        str_i = str(i)
        for i in str_i:
            res += int(i)
        return res        
        
h = Solution()

threshold = 3
rows = 13
cols = 14
r = h.movingCount(threshold, rows, cols)
print(r)