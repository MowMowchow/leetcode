#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    N = len(nums)
      
    low = nums[0]
    high = nums[0]
    ans = nums[0]
    
    for i in range(1, N):
      new_high = max(nums[i], low*nums[i], high*nums[i])
      low = min(nums[i], low*nums[i], high*nums[i])
      
      high = new_high  # updating high right away will make it multiply it by itself for low
      
      ans = max(ans, high)
      
    return ans
    
# @lc code=end

