class Solution:
  def countPyramids(self, grid: List[List[int]]) -> int:
    Nx = len(grid[0])
    Ny = len(grid)
    dp = [[0 for x in range(Nx)] for y in range(Ny)]
    ans = 0
    
    if Ny > 1:
      for ix in range(1, Nx-1):
        if grid[Ny-2][ix] == grid[Ny-1][ix-1] == grid[Ny-1][ix] == grid[Ny-1][ix+1] == 1:
          dp[Ny-2][ix] += 1
          ans += 1
    
    for iy in range(Ny-3, -1, -1):
      for ix in range(1, Nx-1):
        if grid[iy][ix] == grid[iy+1][ix-1] == grid[iy+1][ix] == grid[iy+1][ix+1] == 1:
          ans += 1
          ans += min(dp[iy+1][ix-1], dp[iy+1][ix], dp[iy+1][ix+1])
          dp[iy][ix] += min(dp[iy+1][ix-1], dp[iy+1][ix], dp[iy+1][ix+1]) + 1
  
      
    dp = [[0 for x in range(Nx)] for y in range(Ny)]    

      
    if Ny > 1:
      for ix in range(1, Nx-1):
        if grid[1][ix] == grid[0][ix-1] == grid[0][ix] == grid[0][ix+1] == 1:
          dp[1][ix] += 1
          ans += 1
    
    for iy in range(2, Ny):
      for ix in range(1, Nx-1):
        if grid[iy][ix] == grid[iy-1][ix-1] == grid[iy-1][ix] == grid[iy-1][ix+1] == 1:
          ans += 1
          ans += min(dp[iy-1][ix-1], dp[iy-1][ix], dp[iy-1][ix+1])
          dp[iy][ix] += min(dp[iy-1][ix-1], dp[iy-1][ix], dp[iy-1][ix+1]) + 1
          
          
    return ans