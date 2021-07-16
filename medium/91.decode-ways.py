#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
      if len(s) == 1 and s != "0":
        return 1
      elif not s or s == "0":
        return 0

      N = len(s)
      dp = [0 for x in range(N+1)]
      dp[0] = 1
      dp[1] = 1 if s[0] != "0" else 0

      for i in range(2, N+1):
        a = int(s[i-1])
        b = int(s[i-2])

        if a != 0:
          dp[i] += dp[i-1]
        if 9 < int(str(b)+(str(a))) < 27:  
          dp[i] += dp[i-2]
      
      return dp[N]

# @lc code=end

