#
# @lc app=leetcode id=724 lang=python
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initiate sum to the left and the right
        leftsum, rightsum = 0, sum(nums)

        for i,val in enumerate(nums):
            # iterate from left. withdraw element from rightsum
            rightsum -= val
            #if leftsum == rightsum, return index
            if leftsum == rightsum:
                return i
            # add current element to leftsum
            leftsum += val
        #return -1 if conditions are not met
        return -1
# @lc code=end

