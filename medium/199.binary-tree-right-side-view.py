#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def dfs(self, curr, length, vals):
    if curr.val != None:
      vals = list(vals)
      vals.append(curr.val)
      lvals = list(vals)
      rvals = list(vals)
      if curr.left:
        lvals = self.dfs(curr.left, length+1, lvals)
      if curr.right:
        rvals = self.dfs(curr.right, length+1, rvals)

      if len(lvals) > len(rvals):
        rvals.extend(lvals[len(rvals):])
      
      return rvals


  def rightSideView(self, root: TreeNode) -> List[int]:
    return self.dfs(root, 0, []) if root else []


		
# @lc code=end
