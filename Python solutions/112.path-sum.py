#
# @lc app=leetcode id=112 lang=python
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        return self.hasPathSumWithCurrentSum(root, targetSum, 0)
    
        
    def hasPathSumWithCurrentSum(self, root, targetSum, currentSum):
        if root:
            tempSum = root.val + currentSum
            if tempSum == targetSum:
                if root.left == None and root.right == None:
                    return True
            if self.hasPathSumWithCurrentSum(root.left, targetSum, tempSum):
                return True
            elif self.hasPathSumWithCurrentSum(root.right, targetSum, tempSum):
                return True

# @lc code=end

