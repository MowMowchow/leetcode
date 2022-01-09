class Solution:
  def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
    R = len(grid[0])
    C = len(grid)
    
    arr = [[0 for x in range(R+2)] for y in range(C+2)]
    ans = [[0 for x in range(R+2)] for y in range(C+2)]

    for yi in range(1, C+1):
      for xi in range(1, R+1):
        arr[yi][xi] += grid[yi-1][xi-1]
      
    for yi in range(1, C+1):
      for xi in range(1, R+1):
        arr[yi][xi] += arr[yi][xi-1] + arr[yi-1][xi] - arr[yi-1][xi-1]

    for yi in range(stampHeight, C+1):
      for xi in range(stampWidth, R+1):
        ay = yi-stampHeight+1
        bx = xi-stampWidth+1
        squareSum = arr[yi][xi] - arr[ay-1][xi] - arr[yi][bx-1] + arr[ay-1][bx-1]

        if squareSum == 0:
          ans[yi+1][xi+1] += 1
          ans[ay][xi+1] -= 1
          ans[yi+1][bx] -= 1
          ans[ay][bx] += 1
   
    for yi in range(1, C+1):
      for xi in range(1, R+1):
        ans[yi][xi] += ans[yi][xi-1] + ans[yi-1][xi] - ans[yi-1][xi-1]   
        
        if grid[yi-1][xi-1] == 0 and ans[yi][xi] == 0:
          return False
      
    return True


        
    
        
    
    
    
    