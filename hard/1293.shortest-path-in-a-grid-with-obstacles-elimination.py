class Solution:
  def shortestPath(self, grid: List[List[int]], k: int) -> int:
    R = len(grid)
    C = len(grid[0])
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    vis = {}
    ans = float("inf")
    q = [[0, 0, k, 0]]
    
    while q:
      cx, cy, ck, cl = q.pop(0)
      
      if cx == C-1 and cy == R-1 and ck >= 0:
        ans = min(ans, cl)
        
      if (cx, cy) not in vis:
        vis[(cx, cy)] = -1
      if ck > vis[(cx, cy)] :
        vis[(cx, cy)] = ck
        
        for mx, my in moves:
          nx = cx+mx
          ny = cy+my
          if 0 <= nx < C and 0 <= ny < R:
            if grid[ny][nx] == 0:
              q.append(list([nx, ny, ck, cl+1]))
            elif grid[ny][nx] == 1 and ck > 0:
              q.append(list([nx, ny, ck-1, cl+1]))
    
    return ans if ans != float("inf") else -1