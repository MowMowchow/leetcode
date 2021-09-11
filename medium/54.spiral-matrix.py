#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    R = len(matrix)
    C = len(matrix[0])
    ans = []
    
    for lev in range(R//2):
      for x in range(lev, C-lev):
        ans.append(matrix[lev][x])
      
      for y in range(lev+1, R-lev-1):
        if C-lev-1 >= C//2:
          ans.append(matrix[y][C-lev-1])
        
      for x in range(C-lev-1, lev-1, -1):
        ans.append(matrix[R-lev-1][x])
        
      for y in range(R-lev-2, lev, -1):
        if lev < C//2:
          ans.append(matrix[y][lev])
        
    if R & 1:
      for x in range(R//2, C-(R//2)):
        ans.append(matrix[R//2][x])
    
    return ans
    
# @lc code=end

