class Solution:
  def removeOnes(self, grid: List[List[int]]) -> bool:
    mask = [x for x in grid[0]]
    invMask = [(x+1)%2 for x in grid[0]]
    return all(row == mask or row == invMask for row in grid)
    