#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:24:16 2019

@author: charles
"""

class Solution(object):
    def reOrderArray(self, array):
        """
        :type array: List[int]
        :rtype: void
        """
        l = 0
        r = len(array) - 1
        while l < r:
            while l < r and array[l] % 2 == 1:
                l += 1
            while l < r and array[r] % 2 == 0:
                r -= 1
            array[l], array[r] = array[r], array[l]