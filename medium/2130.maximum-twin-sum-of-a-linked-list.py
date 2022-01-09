# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def pairSum(self, head: Optional[ListNode]) -> int:
    N = 0
    arr = []
    curr = head
    while curr != None:
      N += 1
      arr.append(curr.val)
      curr = curr.next
      
        
    best = 0
    
    for i in range(N//2):
      pair = N-i-1
      best = max(best, arr[i]+arr[pair])
    
    return best
    