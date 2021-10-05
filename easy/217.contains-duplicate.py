#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    vis = {}
    for i in nums:
      if i not in vis:
        vis[i] = 1
      else:
        return True
    return False   

# @lc code=end

