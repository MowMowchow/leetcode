# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cSum = 0
    curr = head
    sectionStart = head
    while curr.next != None:
      
      if curr.val == 0:
        cSum = 0
        currTemp = curr.next
        while currTemp.val != 0:
          cSum += currTemp.val
          currTemp = currTemp.next
        
        curr.val = cSum

        if currTemp.next == None:
          curr.next = None
          return head
        curr.next = currTemp
        curr = curr.next
    
    return head
        
  