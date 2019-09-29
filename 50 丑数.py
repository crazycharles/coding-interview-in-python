# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 19:39:24 2019

@author: an
"""

class Solution(object):
    def getUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly_number = [1]
        two_lst = []
        thr_lst = []
        fiv_lst = []
        if n == 1:
            return ugly_number[-1]
        while len(ugly_number) < n:
            two_lst.append(ugly_number[-1]*2)
            thr_lst.append(ugly_number[-1]*3)
            fiv_lst.append(ugly_number[-1]*5)
            min_v = min([two_lst[0], thr_lst[0], fiv_lst[0]])
            if min_v == two_lst[0]:
                two_lst.pop(0)
            if min_v == thr_lst[0]:
                thr_lst.pop(0)
            if min_v == fiv_lst[0]:
                fiv_lst.pop(0)
            ugly_number.append(min_v)
        return ugly_number[-1]