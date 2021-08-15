#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  
  def dfs(self, curr, total, k):
    if not curr.right and not curr.left:
      if total + curr.val == k:
        return True
    
    res = False
    if curr.left:
      res  = self.dfs(curr.left, total+curr.val, k)
    if res:
      return res
    if curr.right:
      res = self.dfs(curr.right, total+curr.val, k)
      
    return res
  
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
      return 0
    
    return self.dfs(root, 0, targetSum) 
    
# @lc code=end

