# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:17:49 2019

@author: an
"""

class Solution(object):
    def searchArray(self, array, target):
        """
        :type array: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not array:
            return False
        m = len(array[0])
        n = len(array)
        start_x = n - 1
        start_y = 0
        while start_x >= 0 and start_y <= m - 1:
            if array[start_x][start_y] < target:
                start_y += 1
            elif array[start_x][start_y] > target:
                start_x -= 1
            else:
                return True
        return False