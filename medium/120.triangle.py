class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    N = len(triangle)
    if N == 1: return triangle[0][0]
    for i in range(N-2, -1, -1):
      for j in range(i+1):
        triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
    
    return triangle[0][0]