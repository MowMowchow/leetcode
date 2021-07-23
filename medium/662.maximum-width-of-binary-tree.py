#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    N = len(nums)
    mapp = {}
    final = []
    
    for num in nums:
      if num not in mapp:
        mapp[num] = 1
      else:
        mapp[num] += 1
        
    for i in range(N):
      for j in range(i+1, N):
        if i != j:
          if -(nums[i] + nums[j]) in mapp:
            final.append([nums[i], nums[j], -(nums[i]+nums[j])])
    
    return final 
    
# @lc code=end

