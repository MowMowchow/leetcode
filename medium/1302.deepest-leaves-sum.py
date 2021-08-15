#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def dfs(self, curr, depth, arr):
    arr[depth] += curr.val
    
    if curr.left:
      self.dfs(curr.left, depth+1, arr)
    if curr.right:
      self.dfs(curr.right, depth+1, arr)
      
    
  def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    arr = [0 for x in range(10010)]
    ans = 0
    
    self.dfs(root, 1, arr)
    
    for i in range(1, 10002):
      if arr[i] == 0:
        ans = arr[i-1]
        break
        
    return ans
    
# @lc code=end

