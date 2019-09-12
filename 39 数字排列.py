# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:00:25 2019

@author: an
"""

class Solution:
    def permutation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            for j in self.permutation(nums[:i]+nums[i+1:]):
                temp = [nums[i]] + j
                if temp not in res:
                    res.append(temp)
        return res
    
nums = [1,2,3]
h = Solution()

r = h.permutation(nums)
print(r)