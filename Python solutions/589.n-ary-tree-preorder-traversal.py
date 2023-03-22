#
# @lc app=leetcode id=589 lang=python
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root:
            res = [root.val]
            self.preorder2(root, res)
            
            return res
        return []
    
    def preorder2(self, root, res):
        if root:
            for child in root.children:
                res.append(child.val)
                self.preorder2(child, res)
            return res
        return []
# @lc code=end

