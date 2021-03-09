#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
  def climbStairs(self, n: int) -> int:
    dp = [0 for x in range(n+1)]
    dp[0] = 1
    for i in range(1, n+1):
      dp[i] += dp[i-1]
      dp[i] += dp[i-2] if i > 1 else 0
      
    return dp[n]
# @lc code=end

