# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    N = 0
    
    curr = head
    while curr != None:
      curr = curr.next
      N += 1
    if N == 1:
      head.next = None
      head.val = None
      return None
    curr = head
    mid = N//2
    prev = None
    cnt = 0
    
    while curr != None:
      if cnt == mid and prev != None:
        prev.next = curr.next
      prev = curr
      curr = curr.next   
      
      cnt += 1
    
    return head
        