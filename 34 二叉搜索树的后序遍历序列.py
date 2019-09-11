# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:21:27 2019

@author: an
"""

class Solution:
    def verifySequenceOfBST(self, sequence):
        """
        :type sequence: List[int]
        :rtype: bool
        """
        if len(sequence) < 2:
            return True
        root = sequence[-1]
        mid = len(sequence) - 1
        for i in range(len(sequence)):
            if sequence[i] > root:
                mid = i
                break

        for index, element in enumerate(sequence[mid:-1]):
            if element < root:
                return False
        left, right = True, True
        if len(sequence[:mid]) > 0:
            left = self.verifySequenceOfBST(sequence[:mid])
        if len(sequence[mid:]) > 0:
            right = self.verifySequenceOfBST(sequence[mid:-1])
        return  left and right
        
        
        