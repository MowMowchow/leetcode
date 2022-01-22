class Solution:
  def checkValid(self, matrix: List[List[int]]) -> bool:
    vis = {}
    for row in matrix:
      vis = {}
      for num in row:
        if num not in vis:
          vis[num] = 1
      
      if len(vis) != len(matrix):
        return False
      
    for i in range(len(matrix)):
      vis = {}
      for j in range(len(matrix)):
        if matrix[j][i] not in vis:
          vis[matrix[j][i]] = 1
      
      if len(vis) != len(matrix):
        return False
          
    
    return True