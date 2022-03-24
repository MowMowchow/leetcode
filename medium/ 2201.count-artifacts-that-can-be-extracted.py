class Solution:
  def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
    grid = [[2 for x in range(n)] for y in range(n)]
    ans = 0
    for bx, by, tx, ty in artifacts:
      for xi in range(bx, tx+1):
        for yi in range(by, ty+1):
          grid[xi][yi] -= 1
    
    for yi, xi in dig:
      grid[yi][xi] -= 1
  
    
    for bx, by, tx, ty in artifacts:
      good = True
      for xi in range(bx, tx+1):
        for yi in range(by, ty+1):
          if grid[xi][yi]:
            good = False
            break
        if not good:
          break
      
      if good:
        ans += 1
    
    return ans
        