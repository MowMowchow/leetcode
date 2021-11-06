#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    N = len(cost)
    dp = [float("inf") for x in range(N+1)]
    
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    for i in range(2, N):
      for j in range(1, 3):
        dp[i] = min(dp[i], dp[i-j]+cost[i])
        
    return min(dp[N-1], dp[N-2])    
    
# @lc code=end

