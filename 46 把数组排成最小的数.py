# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:07:02 2019
输入：[3, 32, 321]

输出：321323
@author: an
"""

class Solution(object):
    def printMinNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if int(str(nums[j]) + str(nums[j+1])) > int(str(nums[j+1]) + str(nums[j])):
                    nums[j+1], nums[j] = nums[j], nums[j+1]
        res = ""
        for i in nums:
            res += str(i)
        return res
    
    