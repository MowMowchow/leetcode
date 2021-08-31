#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
    N = len(nums)
    for i in range(1, N):
      nums[i] += nums[i-1]
      
    for i in range(N):
      if i == 0:
        if nums[N-1]-nums[0] == 0:
          return 0
      elif i == N-1:
        if nums[N-2] == 0:
          return N-1
      else:
        if nums[i-1] == nums[N-1]-nums[i]:
          return i
      
    return -1
    
# @lc code=end

