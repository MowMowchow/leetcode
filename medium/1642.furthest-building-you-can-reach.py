class Solution:
  def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
    N = len(heights)
    q = []
    ans = 0
    for i in range(N-1):
      if heights[i+1]-heights[i] > 0:
        heappush(q, heights[i+1]-heights[i])
        if len(q) > ladders:
          if ladders == 0:
            bricks -= heights[i+1]-heights[i]
          else:
            bricks -= heappop(q)
      if bricks < 0:
        break
      else:
        ans = max(ans, i+1)
    
    return ans