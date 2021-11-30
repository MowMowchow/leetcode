#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
  def maximalRectangle(self, matrix: List[List[str]]) -> int:
    if not matrix:
      return 0
    
    nX = len(matrix[0])
    nY = len(matrix)
    ans = 0
    dp = [[0 for x in range(nX+1)] for y in range(nY+1)]
    
    for iy in range(1, nY+1):
      for ix in range(1, nX+1):
        if matrix[iy-1][ix-1] == "1":
          dp[iy][ix] += dp[iy][ix-1] + 1
            
          cW = dp[iy][ix]
          for iy2 in range(iy, 0, -1):
            cW = min(cW, dp[iy2][ix])
            ans = max(ans, cW*(iy-iy2+1))
    
      
    return ans   
    
# @lc code=end

