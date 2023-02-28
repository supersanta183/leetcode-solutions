#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []

        def findPair(par):
            if par == ')':
                return '('
            if par == '}':
                return '{'
            if par == ']':
                return '['
            
        def isleft(par):
            if par == '(' or par == '{' or par == '[':
                return True
            return False
        
        for x in s:
            if len(stack)==0 and not isleft(x):
                return False
            if isleft(x):
                stack.append(x)
            else:
                if stack.pop() == findPair(x):
                    continue
                else:
                    return False
        
        if len(stack) == 0:
            return True
        return False

# @lc code=end

