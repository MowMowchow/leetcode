#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
  def fib(self, n: int) -> int:
    dp = [0 for x in range(n+1)]
    
    if n == 0:
      return 0
    
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
      dp[i] = dp[i-1]+dp[i-2]
    
    return dp[n]

# @lc code=end

