#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
  def trap(self, height: List[int]) -> int:
    N = len(height)
    maxr = [0 for x in range(N)]
    maxl = [0 for x in range(N)]
    maxr[N-1] = height[N-1]
    maxl[0] = height[0]
    ans = 0
    
    for i in range(1, N):
      maxl[i] = max(height[i], maxl[i-1])
      
    for i in range(N-2, -1, -1):
      maxr[i] = max(height[i], maxr[i+1])

    for i in range(1, N-1):
      ans += max(min(maxl[i-1], maxr[i+1])-height[i], 0)
      
    return ans
    
# @lc code=end

