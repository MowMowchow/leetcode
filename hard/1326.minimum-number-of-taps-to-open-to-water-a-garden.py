#
# @lc app=leetcode id=1326 lang=python3
#
# [1326] Minimum Number of Taps to Open to Water a Garden
#

# @lc code=start
class Solution:
  def minTaps(self, n: int, ranges: List[int]) -> int:
    intervals = []
    dp = [float("inf") for x in range(n+1)]
    dp[0] = 0
    
    for i in range(n+1):
      a, b = i-ranges[i], i+ranges[i]
      intervals.append(list([max(a, 0), min(b, n)]))
    
    # intervals.sort()
    
    for a, b in intervals:
      for i in range(a, b+1):
        dp[i] = min(dp[i], dp[a]+1 if a > 0 else 1)
    
    return dp[n] if dp[n] != float("inf") else -1
            
# @lc code=end

