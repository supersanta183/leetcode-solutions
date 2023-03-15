#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_dict = {}
        temp = ""
        for index, char in enumerate(s):
            if char not in char_dict and t[index] not in char_dict.values():
                char_dict[char] = t[index]
            if char in char_dict:
                temp += char_dict[char]
        return temp == t
# @lc code=end

