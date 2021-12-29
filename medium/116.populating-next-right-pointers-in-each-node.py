#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
  def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
  
    q = [[root, 0]]

    while q:
      curr, level = q.pop(0)
      if curr:
        if q:
          if q[0][1] == level:
            curr.next = q[0][0]

        if curr.left and curr.right:
          q.append(list([curr.left, level+1]))
          q.append(list([curr.right, level+1]))

    return root

# Constant Space Solution Below:
class Solution:
  def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
  
    def dfs(curr):
      if curr:
        if curr.left and curr.right:
          curr.left.next = curr.right
          if curr.next:
            curr.right.next = curr.next.left
          dfs(curr.left)
          dfs(curr.right)
      
      return root
    
    return dfs(root)

# @lc code=end

