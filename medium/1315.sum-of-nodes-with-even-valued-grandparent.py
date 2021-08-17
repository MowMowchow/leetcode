#
# @lc app=leetcode id=1315 lang=python3
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def dfs(self, curr, total, parentEven):
    if parentEven:
      if curr.left:
        total += curr.left.val 
      if curr.right:
        total += curr.right.val
    
    res = 0
    if curr.left:
      res += self.dfs(curr.left, 0, curr.val%2==0)
    if curr.right:
      res += self.dfs(curr.right, 0, curr.val%2==0)
    
    return res+total


  def sumEvenGrandparent(self, root: TreeNode) -> int:
    return self.dfs(root, 0, False)
    
    
# @lc code=end

