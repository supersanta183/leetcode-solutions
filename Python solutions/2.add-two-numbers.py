#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = int(self.findNumber(l1)[::-1])
        n2 = int(self.findNumber(l2)[::-1])
        res = n1 + n2
        temp = ListNode()
        temp2 = temp

        n = 0
        for i in str(res)[::-1]:
            temp2.val = i
            if n < len(str(res))-1:
                temp2.next = ListNode()
                temp2 = temp2.next
            n += 1
        return temp
    
    def findNumber(self, list):
        if list and list.next:
            return str(list.val) + self.findNumber(list.next)
        return str(list.val)

# @lc code=end

