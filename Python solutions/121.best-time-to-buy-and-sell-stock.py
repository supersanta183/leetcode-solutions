#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur_max, left_index, right_index = 0, 0, 1
        max_value = 0
        while right_index < len(prices):
            if prices[left_index] > prices[right_index]:
                left_index = right_index
            temp = prices[right_index]-prices[left_index]
            cur_max = max(cur_max, temp)
            if cur_max > max_value:
                max_value = cur_max
            right_index += 1
        return max_value

# @lc code=end

