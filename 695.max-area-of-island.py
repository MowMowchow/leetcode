#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
  def dfs(self, cx, cy, total, vis, grid):
    curr_t = 0
    if not vis[cy][cx] and grid[cy][cx]:
      vis[cy][cx] = True 
      curr_t += 1
      moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
      
      for mx, my in moves:
        if 0 <= cx+mx < len(grid[0]) and 0 <= cy+my < len(grid):
          curr_t += self.dfs(cx+mx, cy+my, 0, vis, grid) if grid[cy][cx] else 0
    return curr_t



  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    final = 0
    vis = [[False for x in range(len(grid[0]))] for y in range(len(grid))]

    for i in range(len(grid)): # y
      for j in range(len(grid[0])): # x
        if not vis[i][j] and grid[i][j]:
          final = max(final, self.dfs(j, i, 0, vis, grid))


    return final
    

# @lc code=end

