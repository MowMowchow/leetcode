#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    high1 = -float("inf")

    def dfs(self, curr, total):
      if curr.val != None:
        res1 = max(0, self.dfs(curr.left, 0) if curr.left else 0)
        res2 = max(0, self.dfs(curr.right, 0) if curr.right else 0)

        self.high1 = max(self.high1, res1 + res2 + curr.val)

        return max(res1, res2)+curr.val
      
      else:
        return 0

   
    def maxPathSum(self, root: TreeNode) -> int:
      self.dfs(root, 0) if root else 0
      return self.high1
# @lc code=end

