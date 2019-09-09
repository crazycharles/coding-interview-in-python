# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:25:33 2019

@author: an
一、动态规划做法
i代表绳子的长度，不断增加，一直到length
j代表第一刀从哪里开始剪
剪完之后继续剪下面的i-j吗，如果剪那么结果就是 j*dp[i-j]，如果不剪，那么结果就是 j*(i-j)
取二者最大值就好了，j有1到i种选择，因此要和之前的dp[i]比较，取最大值。
二、公式法
将数字尽可能多的分成3 和 2
"""

class Solution(object):
    def maxProductAfterCutting(self,length):
        """
        :type length: int
        :rtype: int
        """
        dp = [1 for i in range(length+1)]
        for i in range(2, length + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(dp[i - j] * j, j * (i - j)))
        return dp[-1]


class Solution2(object):
    def maxProductAfterCutting(self,length):
        """
        :type length: int
        :rtype: int
        """
        if length == 2:
            return 1
        yu = length % 3
        if yu == 0:
            power = length // 3
            return 3**power
        if yu == 1:
            power = (length - 4) // 3
            return (3**power) * 4
        if yu == 2:
            power = (length - 2) // 3
            return (3**power) * 2    