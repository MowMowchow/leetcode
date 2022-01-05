#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return None
    
    f = head
    s = head
    ins = None
    
    while f.next != None and f.next.next != None:
      f = f.next.next
      s = s.next
      if f == s:
        ins = f
        break
    
    if ins == None:
      return None
    
    s = head
    
    while f != s:
      f = f.next
      s = s.next
      
    return f
      
# @lc code=end

