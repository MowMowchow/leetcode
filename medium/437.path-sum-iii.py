#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    dp = {}
    ans = 0
    if not root:
      return 0
    
    def dfs(c, cs):
      nonlocal ans
      cs += c.val
      
      if targetSum == cs:
        ans += 1
        
      if cs not in dp:
        dp[cs] = 1
      else:
        dp[cs] += 1
      
      if cs-targetSum in dp:
        ans += dp[cs-targetSum]
      
      if c.left:
        dfs(c.left, cs)
        
      if c.right:
        dfs(c.right, cs)
      
      dp[cs] -= 1
    
    dfs(root, 0)
    
    return ans
      
      
  
    
# @lc code=end

