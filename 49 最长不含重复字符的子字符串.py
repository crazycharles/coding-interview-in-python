# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:17:35 2019
输入："abcabc"

输出：3
@author: an
"""
class Solution:
    def longestSubstringWithoutDuplication(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        res = 1
        left = 0
        right = 1
        while left < right and right <= len(s):
            while left < right and right <= len(s) and len(set(s[left:right])) == len(s[left:right]):
                
                res = max(res, right - left)
                right += 1
            while left < right and right <= len(s) and len(set(s[left:right])) != len(s[left:right]):
                left += 1
        return res