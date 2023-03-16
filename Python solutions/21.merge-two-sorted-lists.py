#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = temp = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1, temp = list1.next, list1
            else:
                temp.next = list2
                list2, temp = list2.next, list2

        if list1 or list2:
            temp.next = list1 if list1 else list2
        
        return head.next



# @lc code=end