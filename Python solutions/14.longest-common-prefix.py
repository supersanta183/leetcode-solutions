#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""
        else:
            w1,w2 = max(strs), min(strs)
            i, prefix = 0, 0
            while i<len(w2) and w1[i] == w2[i]:
                i, prefix = i+1, prefix+1
            return w1[0:prefix]

        
# @lc code=end

