#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
class Solution:
  def maxPoints(self, points: List[List[int]]) -> int:
    ans = 0
    N = len(points)
    
    for a in range(N):
      slopes = {}
      ax, ay = points[a]
      for b in range(N):
        if a != b:
          bx, by = points[b]
        
          slope = (by-ay)/(bx-ax) if bx-ax != 0 else float("inf")

          if slope not in slopes:
            slopes[slope] = 1
          else:
            slopes[slope] += 1

          ans = max(ans, slopes[slope])
          
    return ans+1

# @lc code=end

