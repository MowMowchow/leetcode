#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
  def longestPalindromeSubseq(self, s: str) -> int:
    N = len(s)
    rev = s[::-1]
    dp = [[0 for x in range(N+1)] for x in range(N+1)]
    
    for i in range(1, N+1):
      for j in range(1, N+1):
        if s[i-1] == rev[j-1]:
          dp[i][j] = dp[i-1][j-1] + 1
        else:
          dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[N][N]
    
# @lc code=end

