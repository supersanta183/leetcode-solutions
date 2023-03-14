#
# @lc app=leetcode id=1480 lang=python
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            if i == 0:
                nums[i] = nums[i]
            else:
                nums[i] += nums[i-1]
            i += 1
        return nums
# @lc code=end

