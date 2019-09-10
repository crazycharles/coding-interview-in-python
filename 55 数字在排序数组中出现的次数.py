# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:17:12 2019

@author: an
"""

class Solution(object):
    def getNumberOfK(self, nums, k):
        """
        :type nums: list[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] >= k:
                r = m
            else:
                l = m + 1
        # 如果当前没有找到对应的值，那么说明list中没有目标值
        if nums[l] != k:
            return 0
        start = l
        l = start
        r = len(nums) - 1
        while l < r:
            m = (l + r + 1) // 2
            if nums[m] > k:
                r = m - 1
            else:
                l = m
        end = l
        return end - start + 1
    
h = Solution()
nums = [1, 2, 3, 8, 10]
k = 4
r = h.getNumberOfK(nums, k)    
print(r)