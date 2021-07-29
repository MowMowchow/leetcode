#
# @lc app=leetcode id=1465 lang=python3
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#

# @lc code=start
class Solution:
  def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
    horizontalCuts.append(0)
    horizontalCuts.append(h)
    verticalCuts.append(0)
    verticalCuts.append(w)
    HC = len(horizontalCuts)
    VC = len(verticalCuts)
    
    horizontalCuts.sort()
    verticalCuts.sort()
    
    hmax = 0
    vmax = 0
    
    for i in range(1, HC):
      hmax = max(hmax, horizontalCuts[i]-horizontalCuts[i-1])
    
    for i in range(1, VC):
      vmax = max(vmax, verticalCuts[i]-verticalCuts[i-1])
      
    return (hmax*vmax)%(10**9+7)
    
# @lc code=end

