class Solution:#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
  def rob(self, nums: List[int]) -> int:
    N = len(nums)
    dp = [[0 for x in range(2)] for y in range(N+1)]
    
    if N == 1:
      return nums[0]
    
    dp[0][0] = nums[0]
    dp[1][1] = nums[1]
    
    
    for i in range(2, N+1):
      for j in range(2):
        k1 = max(i-2, 0)
        k2 = max(i-3, 0)  
        if not j:
          if i < N-1:
            dp[i][j] = max(dp[k1][j], dp[k2][j])+nums[i]
          else:
            k2 = max(i-1, 0)
            dp[i][j] = max(dp[k1][j], dp[k2][j])

        else:
          if i < N:
            dp[i][j] = max(dp[k1][j], dp[k2][j])+nums[i]
          else:
            k2 = max(i-1, 0)
            dp[i][j] = max(dp[k1][j], dp[k2][j])
            
      
    return max(dp[N][0], dp[N][1])     

# @lc code=end

