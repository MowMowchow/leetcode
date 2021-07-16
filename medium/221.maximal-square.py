#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
      N = len(matrix)
      M = len(matrix[0])
      dp = [[0 for x in range(M+1)] for x in range(N+1)]
      final = 0
      for i in range(1, N+1):
        for j in range(1, M+1):
          if int(matrix[i-1][j-1]):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
            final = max(final, dp[i][j]**2)


        
      return final





# @lc code=end

