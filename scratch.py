class Solution:
  def shortestPath(self, grid: List[List[int]], k: int) -> int:
    R = len(grid)
    C = len(grid[0])
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    