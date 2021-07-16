#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
      vis = {}
      
      while head:
        if head in vis:
          return True
        else:
          vis[head] = True
          head = head.next
          
      return False
      # curr = head.next