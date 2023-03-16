#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        prev, cur, cur_next = None, head, head.next
        while cur_next:
            prev, cur = cur, cur_next
            cur_next = cur.next
            cur.next = prev
        head.next = None
        return cur

# @lc code=end

