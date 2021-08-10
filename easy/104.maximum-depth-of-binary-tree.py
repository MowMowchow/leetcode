#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def dfs(self, curr, depth):
    if not curr:
      return depth-1

    left = self.dfs(curr.left, depth+1)
    right = self.dfs(curr.right, depth+1)
    
    return max(left, right)

  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0

    return self.dfs(root, 1)
    

        
# @lc code=end

