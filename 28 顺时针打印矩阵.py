# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:03:20 2019

@author: an
"""

class Solution(object):
    def printMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        temp = []
        while matrix:
            # 横
            if matrix and matrix[0]:
                temp.extend(matrix.pop(0))
            # 竖
            if matrix and matrix[0]:
                for i in range(len(matrix)):
                    temp.append(matrix[i].pop())
            # 横
            if matrix and matrix[-1]:
                temp.extend(matrix.pop()[::-1])
            else:
                return temp
            # 竖
            if matrix:
                for i in range(len(matrix)-1, -1, -1):
                    temp.append(matrix[i].pop(0))
        return temp
                