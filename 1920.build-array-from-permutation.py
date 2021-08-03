#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution:
  def buildArray(self, nums: List[int]) -> List[int]:
    N = len(nums)
    for i in range(N):
      nums[i] += (nums[nums[i]]%N)*N
    
    for i in range(N):
      nums[i] //= N
      
    return nums
      
# @lc code=end

