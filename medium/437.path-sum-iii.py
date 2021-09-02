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
    ans = 0
    if not root:
      return 0
    
    def dfs(cc, cs):
      nonlocal ans
      cs += cc.val

      if cs == targetSum:
        ans += 1

      if cc.left:
        dfs(cc.left, cs)
      if cc.right:
        dfs(cc.right, cs)
        
    def dfs2(c):
      if c.left:
        dfs2(c.left)
        dfs(c.left, 0)
      if c.right:
        dfs2(c.right)
        dfs(c.right, 0)
         
          
    dfs2(root)
    dfs(root, 0)
    
    return ans 
    
# @lc code=end

