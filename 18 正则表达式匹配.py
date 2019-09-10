# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:02:42 2019

@author: an
"""
#递归做法
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0 and len(p) == 0:
            return True
        if len(s) != 0 and len(p) == 0:
            return False
        if len(p) > 1 and p[1] == "*":
            if len(s) == 0:
                return self.isMatch(s, p[2:])
            else:
                if p[0] == ".":
                    return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
                else:
                    if s[0] == p[0]:
                        return self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
                    else:
                        return self.isMatch(s, p[2:])
        if len(p) > 1 and p[1] != "*":
            if len(s) == 0:
                return False
            else:
                if p[0] == ".":
                    return self.isMatch(s[1:], p[1:])
                else:
                    if s[0] == p[0]:
                        return self.isMatch(s[1:], p[1:])
                    else:
                        return False
        if len(p) == 1:
            if len(s) == 0:
                return False
            else:
                if p[0] == ".":
                    return self.isMatch(s[1:], p[1:])
                else:
                    if s[0] == p[0]:
                        return self.isMatch(s[1:], p[1:])
                    else:
                        return False

h = Solution()
s = "aaaa"
p = "b*"
r = h.isMatch(s, p)
print(r)