class Solution:
  def bfs(self, sx, sy, visited, grid, N, M): # N=num of rows
    q = [[sx, sy]]
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    while q:
      cx, cy = q.pop(0)
      if not visited[cy][cx]:
        visited[cy][cx] = True
        for mx, my in moves:
          if 0 <= cy+my < N and 0 <= cx+mx < M:
            if grid[cy+my][cx+mx] == "1":
              q.append(list([cx+mx, cy+my]))
  
  
  def numIslands(self, grid: List[List[str]]) -> int:
      # M + N
    N = len(grid)
    M = len(grid[0])
    visited = [[False for x in range(M)] for y in range(N)]

    cnt = 0
    for i in range(N):
      for j in range(M):
        if not visited[i][j] and grid[i][j] == "1":
          self.bfs(j, i, visited, grid, N, M)
          cnt += 1

    return cnt