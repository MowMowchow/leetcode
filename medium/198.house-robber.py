#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
  def rob(self, nums: List[int]) -> int:
    N = len(nums)  
    dp = [0 for x in range(N)]
    
    if N < 3:
      return max(nums)
    
    dp[0] = nums[0]
    
    for i in range(1, N):
      dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    

    return dp[N-1]

# @lc code=end

