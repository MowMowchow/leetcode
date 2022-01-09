#
# @lc app=leetcode id=1024 lang=python3
#
# [1024] Video Stitching
#

# @lc code=start
class Solution:
  def videoStitching(self, clips: List[List[int]], time: int) -> int:
    N = len(clips)
    dp = [float("inf") for x in range(time+1)]
    dp[0] = 0
    
    for i in range(time+1):
      for a, b in clips:
        if a <= i <= b:
          dp[b] = min(dp[i], dp[a]+1)
    print(dp)
    return dp[time] if dp[time] != float("inf") else -1    

# @lc code=end

