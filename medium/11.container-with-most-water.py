#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
  def maxArea(self, height: List[int]) -> int:
    N = len(height)
    # keep a left and right pointer that start at 0 and N-1 respectively 
    #   if our left line is < our right line, then increment the left line
    #   otherwise increment the right line
    # update answer

    ans = 0
    l = 0
    r = N-1
    
    while l < r:
      ans = max(ans, min(height[l], height[r])*(r-l))
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1
    
    return ans   

# @lc code=end

