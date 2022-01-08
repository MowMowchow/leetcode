#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
  def jump(self, nums: List[int]) -> int:
    N = len(nums)
    dp = [float("inf") for x in range(N+1)]
    dp[0] = 0
    
    for i in range(N):
      for j in range(i, min(i+nums[i]+1, N)):
          dp[j] = min(dp[j], dp[i]+1)

    return dp[N-1]   

# @lc code=end

