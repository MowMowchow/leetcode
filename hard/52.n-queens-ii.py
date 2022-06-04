class Solution:
  def totalNQueens(self, n: int) -> List[List[str]]:
    ansPoints = 0
    inf = float("inf")
    
    
    def rec(x, y, points):
      nonlocal ansPoints
      if y == n:
        ansPoints += 1
        return
      for x in range(n):
        vertLine = (inf, inf, x, inf)
        horzLine = (y, inf, inf, y)
        downSlope = (inf, -1, inf, x+y)
        upSlope = (inf, 1, inf, x-y)
        
        if (not vertLine in vis) and (not horzLine in vis) and (not downSlope in vis) and (not upSlope in vis):
          vis[vertLine] = 1
          vis[horzLine] = 1
          vis[downSlope] = 1
          vis[upSlope] = 1
          
          rec(x, y+1, points + list([[x, y]]))
          
          del vis[vertLine]
          del vis[horzLine]
          del vis[downSlope]
          del vis[upSlope]      

          
    vis = {}
    rec(0, 0, [])
    
    return ansPoints
        