# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:29:54 2019

@author: an
"""

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        # 去除首尾重复数字
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < nums[0]:
                index = i
                nums = nums[:index+1]
                break
        # 判断是否为升序序列
        if nums[-1] > nums[0]:
            return nums[0]
        l = 0 
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] <= nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

h = Solution()
nums = [1,1,1,0,1,1,1,1,1]
r = h.findMin(nums)
print(r)