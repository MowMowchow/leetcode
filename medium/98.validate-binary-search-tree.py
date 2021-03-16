#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def dfs(self, curr):
    # print("curr at:", curr.val, ", left:", curr.left, ", right:", curr.right)
    left = [False, curr.val, curr.val] # [1]: largest min, [2] smallest max
    right = [False, curr.val, curr.val]
    if curr.val != None:
      if curr.left:
        if curr.left.val < curr.val:
          left = self.dfs(curr.left)
          
      else:
        left[0] = 'x'

      if curr.right:
        if curr.right.val > curr.val:
          right = self.dfs(curr.right)
      else:
        right[0] = 'x'

      left[1] = min(left[1], curr.val)
      right[2] = max(right[2], curr.val)
      if left[0] == False or right[0] == False:
        return [False, left[1], right[2]]
      elif (left[0] == 'x' and right[0] != 'x'):
        return [curr.val < right[1] <= right[2], left[1], right[2]]
      elif (left[0] != 'x' and right[0] == 'x'):
        return [left[1] <= left[2] < curr.val, left[1], right[2]]
      elif (left[0] == 'x' and right[0] == 'x'):
        return [True, min(left[1], curr.val), left[1], right[2]]

      return [(left[0] and right[0]) and (left[1] <= left[2] < curr.val < right[1] <= right[2]), left[1], right[2]]


  def isValidBST(self, root: TreeNode) -> bool:
    res = self.dfs(root)
    # print(res)
    return res[0]
# @lc code=end

