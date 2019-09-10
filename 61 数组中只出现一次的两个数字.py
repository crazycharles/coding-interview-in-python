# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:27:06 2019

@author: an
"""

class Solution(object):
    def findNumsAppearOnce(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        map = {}
        res = []
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
        for i in map.keys():
            if map[i] == 1:
                res.append(i)
        return res