#
# @lc app=leetcode id=392 lang=python
#
# [392] Is Subsequence
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        temp = t
        for char in s:
            if char not in temp:
                return False
            temp = temp[temp.find(char)+1:len(temp)]
        return True
# @lc code=end

