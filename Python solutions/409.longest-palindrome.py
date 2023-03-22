#
# @lc app=leetcode id=409 lang=python
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize a dictionary to store the frequency of each character in the string
        freq_dict = {}
        for char in s:
            freq_dict[char] = freq_dict.get(char, 0) + 1
        
        # Initialize a variable 'length' to 0, which will store the length of the longest palindrome
        length = 0
        
        # Iterate through the dictionary and add up the length of all even-frequency characters
        for freq in freq_dict.values():
            length += freq // 2 * 2
        
        # Check if there are any characters whose frequency is odd. If yes, add one of them to the length
        if any(freq % 2 == 1 for freq in freq_dict.values()):
            length += 1
        
        # Return the length as the answer
        return length
# @lc code=end

