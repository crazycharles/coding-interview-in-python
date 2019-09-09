# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:40:05 2019

@author: an
"""

class Solution(object):
    def __init__(self):
        self.directions = [[0,-1],[0,1],[1,0],[-1,0]]
    def hasPath(self, matrix, string):
        """
        :type matrix: List[List[str]]
        :type string: str
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix[0])        
        n = len(matrix)
        for i in range(n):
            for j in range(len(matrix[i])):
                if self.dfs(matrix, string, 0, i, j):
                    return True
        return False
    def dfs(self, matrix, string, u, i, j):
        if matrix[i][j] != string[u]:
            return False
        if u == len(string) - 1:
            return True
        t = matrix[i][j]
        matrix[i][j] = "*"
        for direction in self.directions:
            a = i + direction[0]
            b = j + direction[1]
            
            if a >= 0 and a < len(matrix) and b >= 0 and b < len(matrix[a]):
                if self.dfs(matrix, string, u+1, a, b):
                    return True
        matrix[i][j] = t