#
# @lc app=leetcode id=876 lang=python
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, count = head, 0

        while cur.next:
            count += 1
            cur = cur.next
        
        cur = head
        for i in range(-(-count//2)):
            cur = cur.next
        return cur
# @lc code=end

