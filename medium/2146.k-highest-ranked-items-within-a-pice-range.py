class Solution:
  def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
    R = len(grid)
    C = len(grid[0])
    
    vis = {}
    items = []
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    
    q = [list([start[1], start[0], 0])]
    
    while q:
      cx, cy, cd = q.pop(0)
      if (cx, cy) not in vis and 0 <= cx < C and 0 <= cy < R:
        vis[(cx, cy)] = 1
        if pricing[0] <= grid[cy][cx] <= pricing[1]:
          items.append(list([cd, grid[cy][cx], cy, cx]))
          
        for mx, my in moves:
          if 0 <= cx+mx < C and 0 <= cy+my < R:
            if grid[cy+my][cx+mx] > 0:
              q.append(list([cx+mx, cy+my, cd+1]))    

    items.sort()
    return [[items[x][-2], items[x][-1]] for x in range(min(len(items), k))]           
    